import sys
import requests
import argparse
from colorama import Fore, Style, init
import signal
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize colorama
init()

# Global variables
results = []
vulnerabilities = []
stop_event = threading.Event()
args = None  # Global args

# Handle Ctrl+C interruption
def signal_handler(sig, frame):
    print(f"\n{Fore.YELLOW}Interrupt received. Exiting...{Style.RESET_ALL}")
    stop_event.set()
    save_results(args)  # Pass args to save_results
    sys.exit(0)

# Setup signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def banner():
    print(f"""
    {Fore.GREEN}#############################################
    # Welcome to SecProbeX                      #
    # Version: 1.0.0                            #
    # Author: coffin0x                          #
    # License: MIT                              #
    #############################################{Style.RESET_ALL}
    """)

# Load payloads for the specific type of test
def load_payloads(test_type):
    payloads = []

    try:
        if test_type == 'paths':
            with open(f'payloads/path.txt', 'r') as file:
                payloads = file.read().splitlines()
        else:
            with open(f'payloads/{test_type}.txt', 'r') as file:
                payloads = file.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Payload file for {test_type} not found.{Style.RESET_ALL}")

    return payloads

# Parameter discovery
def find_parameters(url):
    if '?' in url:
        params = url.split('?')[1].split('&')
        return [param.split('=')[0] for param in params]
    return []

# Subdomain finding
def find_subdomains(domain, payloads):
    if not payloads:
        print(f"{Fore.RED}Payload file for subdomains not found.{Style.RESET_ALL}")
        return []

    subdomains = []
    def check_subdomain(payload):
        test_url = f"http://{payload}.{domain}"
        try:
            response = requests.get(test_url, timeout=3)
            if response.status_code == 200:
                return test_url
        except requests.RequestException:
            return None

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_subdomain, payload) for payload in payloads]
        for future in as_completed(futures):
            result = future.result()
            if result:
                subdomains.append(result)
    
    if subdomains:
        print(f"{Fore.GREEN}Found subdomains:{Style.RESET_ALL}")
        for subdomain in subdomains:
            print(f"{Fore.GREEN}{subdomain}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}No subdomains found.{Style.RESET_ALL}")

    return subdomains

# Path finding
def find_paths(domain, payloads):
    if not payloads:
        print(f"{Fore.RED}Payload file for paths not found.{Style.RESET_ALL}")
        return []

    paths = []
    def check_path(payload):
        test_url = f"http://{domain}/{payload}"
        try:
            response = requests.get(test_url, timeout=3)
            if response.status_code == 200:
                return test_url
        except requests.RequestException:
            return None

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_path, payload) for payload in payloads]
        for future in as_completed(futures):
            result = future.result()
            if result:
                paths.append(result)
    
    if paths:
        print(f"{Fore.GREEN}Found paths:{Style.RESET_ALL}")
        for path in paths:
            print(f"{Fore.GREEN}{path}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}No paths found.{Style.RESET_ALL}")

    return paths

# Testing function
def test_payload(url, param, payload, test_type):
    if stop_event.is_set():
        return
    
    test_url = url.replace(f"{param}=", f"{param}={payload}")
    try:
        response = requests.get(test_url, timeout=5)
    except requests.RequestException:
        return f"{Fore.RED}[Error] Failed to request URL: {test_url}{Style.RESET_ALL}"
    
    result = f"{Fore.RED}[Not Vulnerable] Parameter: {param} -> {test_url} (Payload: {payload}){Style.RESET_ALL}"
    if test_type == 'lfi' and ("root:x" in response.text or "root" in response.text):
        result = f"{Fore.GREEN}[Vulnerable] LFI detected in parameter: {param} -> {test_url} (Payload: {payload}){Style.RESET_ALL}"
        vulnerabilities.append(result)
    elif test_type == 'sqli' and ("syntax" in response.text or "SQL" in response.text or "mysql" in response.text):
        result = f"{Fore.GREEN}[Vulnerable] SQLi detected in parameter: {param} -> {test_url} (Payload: {payload}){Style.RESET_ALL}"
        vulnerabilities.append(result)
    elif test_type == 'xss' and payload in response.text:
        result = f"{Fore.GREEN}[Vulnerable] XSS detected in parameter: {param} -> {test_url} (Payload: {payload}){Style.RESET_ALL}"
        vulnerabilities.append(result)
    elif test_type == 'ssti' and payload in response.text:
        result = f"{Fore.GREEN}[Vulnerable] SSTI detected in parameter: {param} -> {test_url} (Payload: {payload}){Style.RESET_ALL}"
        vulnerabilities.append(result)
    
    return result

# Save results to file
def save_results(args):
    if args.output:
        with open(args.output, 'w') as file:
            for result in vulnerabilities:
                file.write(result + '\n')
        print(f"{Fore.GREEN}Results saved to {args.output}{Style.RESET_ALL}")

# Scanning URL for selected vulnerability
def scan_url(url, test_type, payloads):
    params = find_parameters(url)
    if not params:
        print("No parameters found to test.")
        return []

    print(f"Found parameters: {params}")

    results.clear()  # Clear previous results
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for param in params:
            for payload in payloads:
                future = executor.submit(test_payload, url, param, payload, test_type)
                futures.append(future)
        
        for future in as_completed(futures):
            if stop_event.is_set():
                break
            result = future.result()
            print(result)
            results.append(result)
    
    return results

# Main function
def main():
    global args
    banner()
    
    parser = argparse.ArgumentParser(
        description='SecProbeX: A tool for performing various types of vulnerability scans such as subdomain enumeration, path discovery, LFI (Local File Inclusion), SQLi (SQL Injection), XSS (Cross-Site Scripting), and SSTI (Server-Side Template Injection).'
    )
    parser.add_argument('-o', '--output', help='File to save results', type=str, default=None)
    args = parser.parse_args()

    print("\nSelect the type of testing to perform:")
    print("1. Subdomain Finder")
    print("2. Path Finder")
    print("3. LFI (Local File Inclusion)")
    print("4. SQLi (SQL Injection)")
    print("5. XSS (Cross-Site Scripting)")
    print("6. SSTI (Server-Side Template Injection)")
    
    try:
        test_type_choice = int(input("Enter your choice (1/2/3/4/5/6): "))
        payloads = []

        if test_type_choice == 1:
            payloads = load_payloads('subdomain')
            domain = input("Enter the domain to find subdomains (e.g., example.com): ")
            find_subdomains(domain, payloads)
        elif test_type_choice == 2:
            payloads = load_payloads('paths')  # This will now load 'path.txt'
            domain = input("Enter the domain to find paths (e.g., example.com): ")
            find_paths(domain, payloads)
        elif test_type_choice == 3:
            payloads = load_payloads('lfi')
            url = input("Enter the URL to test (e.g., https://example.com?page=): ")
            scan_url(url, 'lfi', payloads)
        elif test_type_choice == 4:
            payloads = load_payloads('sqli')
            url = input("Enter the URL to test (e.g., https://example.com?page=): ")
            scan_url(url, 'sqli', payloads)
        elif test_type_choice == 5:
            payloads = load_payloads('xss')
            url = input("Enter the URL to test (e.g., https://example.com?page=): ")
            scan_url(url, 'xss', payloads)
        elif test_type_choice == 6:
            payloads = load_payloads('ssti')
            url = input("Enter the URL to test (e.g., https://example.com?page=): ")
            scan_url(url, 'ssti', payloads)
        else:
            print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")

    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")

    save_results(args)

if __name__ == "__main__":
    main()

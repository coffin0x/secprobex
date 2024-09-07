# SecProbeX

SecProbeX is a comprehensive security testing tool designed to perform extensive vulnerability assessments. It features capabilities for subdomain enumeration, path discovery, and various injection tests, including Local File Inclusion (LFI), SQL Injection (SQLi), Cross-Site Scripting (XSS), and Server-Side Template Injection (SSTI).

## Features

- **Subdomain Finder**: Efficiently enumerates subdomains using predefined payloads.
- **Path Finder**: Discovers valid paths on a target domain to identify potential entry points.
- **LFI (Local File Inclusion)**: Detects Local File Inclusion vulnerabilities that could allow unauthorized file access.
- **SQLi (SQL Injection)**: Identifies SQL Injection vulnerabilities that can compromise database integrity.
- **XSS (Cross-Site Scripting)**: Checks for Cross-Site Scripting vulnerabilities that might lead to malicious script execution.
- **SSTI (Server-Side Template Injection)**: Assesses vulnerabilities in server-side template engines that could lead to remote code execution.

## Installation

### Clone the Repository

Begin by cloning the SecProbeX repository to your local machine:

```bash
git clone https://github.com/coffin0x/secprobex.git
cd secprobex
```

### Install Dependencies
Install the necessary Python libraries using pip:

```
pip install -r requirements.txt
```

## Payloads

The `payloads` folder contains crucial payload files required for different tests. Ensure the folder has the following files:

- `subdomains.txt`: Contains payloads for subdomain enumeration.
- `path.txt`: Contains payloads for discovering valid paths.
- `lfi.txt`: Contains payloads for Local File Inclusion tests.
- `sqli.txt`: Contains payloads for SQL Injection tests.
- `xss.txt`: Contains payloads for Cross-Site Scripting tests.
- `ssti.txt`: Contains payloads for Server-Side Template Injection tests.

## Usage

### Step-by-Step Instructions

1. **Run the Tool**: Execute SecProbeX with the following command:
   ```
   python3 secprobex.py
   ```
2. **Select the Test Type**: The tool will prompt you to choose the type of test. Enter the number corresponding to your choice:
   ```
   Choose the type of test:
   1. Subdomain Finder
   2. Path Finder
   3. LFI (Local File Inclusion)
   4. SQLi (SQL Injection)
   5. XSS (Cross-Site Scripting)
   6. SSTI (Server-Side Template Injection)
   ```

3. **Enter the Target URL**: You will be asked to provide the target URL for testing. Enter the URL and press Enter. For example:
   ```
   https://example.com?param=test
   ```
   
4. **Review the Results**: The tool will execute the selected test and display results, indicating whether the target is vulnerable.

## Example Workflow

```
$ python3 secprobex.py
Choose the type of test:
1. Subdomain Finder
2. Path Finder
3. LFI (Local File Inclusion)
4. SQLi (SQL Injection)
5. XSS (Cross-Site Scripting)
6. SSTI (Server-Side Template Injection)
Enter choice: 5
Enter the target URL: https://example.com?param=test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

Developed by *coffin0x*.

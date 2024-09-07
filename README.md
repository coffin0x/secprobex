# SecProbeX

SecProbeX is a robust security testing tool designed for comprehensive vulnerability assessment. It provides functionality for subdomain enumeration, path discovery, and various types of injections, including Local File Inclusion (LFI), SQL Injection (SQLi), Cross-Site Scripting (XSS), and Server-Side Template Injection (SSTI).

## Features

- **Subdomain Finder**: Efficiently enumerates subdomains using predefined payloads.
- **Path Finder**: Discovers valid paths on a target domain.
- **LFI (Local File Inclusion)**: Identifies Local File Inclusion vulnerabilities.
- **SQLi (SQL Injection)**: Detects SQL Injection vulnerabilities.
- **XSS (Cross-Site Scripting)**: Checks for Cross-Site Scripting vulnerabilities.
- **SSTI (Server-Side Template Injection)**: Assesses Server-Side Template Injection vulnerabilities.

## Installation

### Clone the Repository

To get started, clone the SecProbeX repository:

```bash
git clone https://github.com/coffin0x/secprobex.git
cd secprobex
```

### Install Dependencies

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

## Payloads

The payloads folder contains essential payload files required for various tests. Ensure the folder includes the following files:

- subdomains.txt for subdomain enumeration.
- lfi.txt for Local File Inclusion tests.
- sqli.txt for SQL Injection tests.
- xss.txt for Cross-Site Scripting tests.

## Usage

### Running the Tool

Execute SecProbeX with the following command:

```bash
python3 secprobex.py
```

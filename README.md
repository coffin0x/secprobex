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

### Payloads

The `payloads` folder contains essential payload files required for various tests. Ensure that the following files are present in the folder:

- `subdomains.txt`: Used for subdomain enumeration.
- `lfi.txt`: Used for Local File Inclusion (LFI) tests.
- `sqli.txt`: Used for SQL Injection (SQLi) tests.
- `xss.txt`: Used for Cross-Site Scripting (XSS) tests.

### Usage

#### Step-by-Step Instructions:

1. **Run the Tool**: Use the following command to execute SecProbeX:

   ```bash
   python3 secprobex.py
   ```
   After starting the tool, you will be presented with options to choose the type of test:

```markdown
1. Subdomain Finder
2. Path Finder
3. LFI (Local File Inclusion)
4. SQLi (SQL Injection)
5. XSS (Cross-Site Scripting)
6. SSTI (Server-Side Template Injection)
```

Enter the number corresponding to the test you want to perform. For example, to perform an XSS test, input:

```bash
5
```

The tool will then prompt you to enter the URL to be tested. Provide the target URL and press Enter. For example:

```bash
https://example.com?param=
```

The tool will run the specified test and display the results, indicating whether the target is vulnerable or not.

### Example Workflow

```bash
$ python3 secprobex.py
```

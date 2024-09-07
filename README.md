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

### Example Workflow

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

## Getting Started

To get started with SecProbeX, follow these steps:

1. **Clone the Repository**: Use the command provided in the [Installation](#installation) section.
2. **Install Dependencies**: Install the required Python libraries using pip.
3. **Prepare Payloads**: Ensure the `payloads` folder contains the necessary files.
4. **Run the Tool**: Execute the tool and follow the [Step-by-Step Instructions](#step-by-step-instructions) to perform tests.

## Configuration

SecProbeX does not require additional configuration beyond setting up the payload files. If future versions include configurable settings, instructions will be provided here.

## Troubleshooting

If you encounter issues with SecProbeX, consider the following:

- **Dependencies Not Installed**: Ensure all required libraries are installed using `pip install -r requirements.txt`.
- **File Not Found**: Verify that all necessary payload files are present in the `payloads` folder.
- **Permission Issues**: Run the tool with appropriate permissions if you encounter access-related errors.

## Contributing

Contributions to SecProbeX are welcome! If you have suggestions or improvements, please submit a pull request. Ensure that your changes are well-documented and tested before submitting.

## Contact

For any questions or feedback, you can reach out to me via:

- **Email**: your.email@example.com
- **GitHub**: [coffin0x](https://github.com/coffin0x)

## Acknowledgements

- Thanks to the open-source community for the libraries and tools used in SecProbeX.
- Special thanks to contributors and testers who provided valuable feedback.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

Developed by *coffin0x*.

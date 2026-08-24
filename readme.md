![logo](https://github.com/nomankarim8/nomankarim8/blob/main/image.png?raw=true)

 


 
 

# 🛡️  Admin Panel Finder

---

## 📌 Overview

**Enhanced Admin Panel Finder** is a Python-based web endpoint discovery utility that checks a target domain against a customizable list of URL paths.

It is designed to help security researchers and developers quickly identify endpoints that return potentially interesting HTTP responses, including:

- `200 OK` — Successful response
- `401 Unauthorized` — Authentication required
- `3xx` — Redirect responses

The tool uses multithreading to perform checks concurrently, making it significantly faster than a sequential implementation.

> **⚠️ Important:** This tool must only be used against websites, applications, or infrastructure that you own or have explicit authorization to test.

---

## ✨ Key Features

| FeatureDescription          |                                                       |
| --------------------------- | ----------------------------------------------------- |
| ⚡ Multithreading            | Concurrent endpoint checking for improved performance |
| 🌐 HTTP/HTTPS               | Supports both HTTP and HTTPS targets                  |
| 📊 Progress Tracking        | Displays real-time scanning progress                  |
| 🔎 Status Detection         | Identifies `200`, `401`, and `3xx` responses          |
| ↪️ Redirect Detection       | Displays redirect destinations when available         |
| 🔐 Authentication Detection | Identifies endpoints requiring authentication         |
| 📝 Custom Wordlist          | Uses a user-defined `link.txt` file                   |
| 🛡️ Error Handling          | Handles common network and HTTP errors                |
| 🤖 Custom User-Agent        | Sends a browser-like HTTP User-Agent                  |
| 🧩 Zero Dependencies        | Uses only Python standard-library modules             |

---

## 🏗️ Project Structure

```
Admin-Panel-Finder/
│
├── admin_panel_finder.py    # Main scanner
├── link.txt                 # Endpoint/path wordlist
├── README.md                # Documentation
└── LICENSE                  # Project license

```

---

## 💻 Requirements

### Software

- Python **3.8+**
- Internet/network connectivity
- An authorized target environment

### Dependencies

No third-party Python packages are required.

The project uses Python's built-in modules:

```
urllib.request
urllib.error
concurrent.futures
sys

```

---

## 🚀 Installation

### 1. Clone the repository

```
git clone https://github.com/nomankarim8/Admin-Panel-Finder.git

```

### 2. Enter the project directory

```
cd Admin-Panel-Finder

```

### 3. Verify Python

```
python --version

```

On some systems:

```
python3 --version

```

---

## 📝 Configure the Endpoint Wordlist

The scanner reads endpoint paths from:

```
link.txt

```

Example:

```
admin/
admin/login
admin/login.php
administrator/
admin-panel/
backend/
dashboard/
login/
panel/

```

You can add or remove paths according to the application you are authorized to test.

### Example

```
admin/
administrator/
dashboard/
management/
control-panel/
backend/
staff/

```

---

# ▶️ Usage

Run the scanner with:

```
python admin_panel_finder.py

```

The program will display the banner and ask for the target.

### Target

```
Enter Site Name (ex: example.com or www.example.com):

```

Example:

```
example.com

```

### Protocol

```
Use HTTPS? (y/n, default n):

```

For HTTPS:

```
y

```

For HTTP:

```
n

```

### Threads

```
Number of threads (default 20):

```

Example:

```
20

```

---

## 📊 Example Session

```
🛡️=======================================🛡️
|     Enhanced Admin Panel Finder Tool    |
|       Original by: nomankarim8          |
|      Improved for better performance    |
|      For Legal & Ethical Use Only       |
🛡️=======================================🛡️

Enter Site Name (ex: example.com or www.example.com): example.com

Use HTTPS? (y/n, default n): y

Number of threads (default 20): 20

Scanning https://example.com with 8 paths using 20 threads...

Progress: 8/8 paths checked

Results:

[FOUND 200] => https://example.com/admin/
[AUTH REQUIRED 401] => https://example.com/dashboard/
[REDIRECT 301] => https://example.com/login/ -> /login

```

---

# 🔎 HTTP Response Handling

The scanner focuses on several response categories.

### `200 OK`

```
[FOUND 200] => https://example.com/admin/

```

The server successfully returned the requested resource.

**Important:** A `200` response alone does not prove that the endpoint is an administrative panel.

---

### `401 Unauthorized`

```
[AUTH REQUIRED 401] => https://example.com/dashboard/

```

The endpoint requires authentication.

This can be useful during an authorized security assessment to identify protected application areas.

---

### `3xx Redirect`

```
[REDIRECT 301] => https://example.com/login/

```

The server redirected the request.

When available, the tool also displays the `Location` header:

```
[REDIRECT 301] => https://example.com/admin -> /login

```

---

# ⚙️ Performance

The scanner uses Python's:

```
concurrent.futures.ThreadPoolExecutor

```

Instead of checking endpoints sequentially, multiple requests can be processed concurrently.

### Example

With:

```
100 endpoints
20 threads

```

the scanner can process multiple endpoint checks simultaneously.

### Recommended Thread Counts

| EnvironmentSuggested Threads      |                  |
| --------------------------------- | ---------------- |
| Local development server          | 5–10             |
| Small authorized test environment | 10–20            |
| Normal authorized assessment      | 10–30            |
| Large/controlled environment      | Adjust carefully |

> Higher concurrency does not always mean better performance. Excessive requests may overload a server or trigger rate limiting.

---

# 🧠 How It Works

The basic workflow is:

```
             ┌────────────────────┐
             │     Start Tool     │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │   Read link.txt    │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │   Enter Target     │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Select HTTP/HTTPS  │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Create Thread Pool │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Check Each Path    │
             └─────────┬──────────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
           200        401       3xx
             │         │         │
             └─────────┼─────────┘
                       ▼
             ┌────────────────────┐
             │ Display Results    │
             └────────────────────┘

```

---

# 🔐 Security & Ethical Use

This project is intended for legitimate security and development purposes, including:

- ✅ Testing your own website
- ✅ Authorized penetration testing
- ✅ Security research with permission
- ✅ Internal application assessment
- ✅ Local development environments
- ✅ CTF and cybersecurity laboratories
- ✅ Educational security testing

### Do Not Use Against:

- ❌ Websites you do not own
- ❌ Systems without authorization
- ❌ Third-party infrastructure without permission
- ❌ Production systems where scanning has not been approved

Unauthorized scanning may violate organizational policies, terms of service, or applicable laws.

**You are responsible for ensuring that your use of this software is lawful and authorized.**

---

# ⚠️ Limitations

This tool is intentionally lightweight and should not be considered a complete web vulnerability scanner.

It does **not**:

- Exploit discovered endpoints
- Bypass authentication
- Attempt password guessing
- Perform vulnerability exploitation
- Guarantee that a discovered path is an admin panel
- Detect every possible endpoint
- Replace professional penetration-testing tools

A discovered endpoint should always be manually reviewed in an authorized environment.

---

# 🛠️ Troubleshooting

### `link.txt not found`

You may see:

```
Error: 'link.txt' not found!

```

Make sure the file exists in the same directory as the Python script:

```
Admin-Panel-Finder/
├── admin_panel_finder.py
└── link.txt

```

---

### `link.txt is empty`

If the file contains no valid paths:

```
Warning: 'link.txt' is empty!

```

Add one endpoint per line.

---

### Connection Errors

Network errors may occur because of:

- DNS problems
- Firewall restrictions
- Server downtime
- SSL/TLS configuration
- Network connectivity
- Rate limiting

The current implementation intentionally ignores many connection errors so the scan can continue.

---

# 📈 Possible Future Improvements

Potential enhancements for future releases:

-  Command-line arguments
-  Automatic HTTP/HTTPS detection
-  Configurable request timeout
-  JSON output
-  CSV export
-  Colored terminal output
-  Custom User-Agent option
-  Retry mechanism
-  Rate limiting
-  Proxy support
-  Detailed response-size analysis
-  Content fingerprinting
-  Duplicate result filtering
-  Configurable status-code detection
-  Structured logging
-  Better CLI interface with `argparse`

---

# 🤝 Contributing

Contributions are welcome.

If you want to improve the project:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes in an authorized environment.
5. Commit your changes.
6. Open a pull request.

Example:

```
git checkout -b feature/improved-output

```

---

# 📜 License

This project is provided for educational and authorized security-testing purposes.

See the repository's `LICENSE` file for the applicable licensing terms.

---

# 👨‍💻 Author

### Noman Karim

**GitHub:** `nomankarim8`

**Project:** Enhanced Admin Panel Finder

---

## ⭐ Support the Project

If you find this project useful for legitimate security testing or learning:

- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest improvements
- 🤝 Contribute responsibly

---

# 🔐 HTTPS Checker

A Python CLI tool to check if a website uses HTTPS and whether all external resources (images, scripts, stylesheets) are also loaded securely.

---

## ✅ Features

- Verifies if the website uses HTTPS
- Parses the page to check for insecure (`http://`) resources
- Reports any mixed content issues
- CLI-based tool: easy to use during audits

---

## 🛠 Tech Used

- Python `requests`
- `BeautifulSoup` (bs4)
- `urllib.parse` for resource handling

---

## 🚀 How to Run

### 1. Clone the repository

```bash
https://github.com/Aditi-Rani/https-checker
```
```bash
cd https-checker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the script
```bash
python https_checker.py
```

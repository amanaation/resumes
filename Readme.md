# 📧 Email Group Sender

This Python project reads a list of email addresses from a CSV file, groups recipients from the same company (based on their email domain), and sends **one email per company**, placing all recipients in **BCC**.

---

## 🧰 Prerequisites

Before setting up the project, make sure you have the following installed:

### 1. Install Python

#### 🔹 Windows
1. Go to the official Python download page: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest version of **Python 3**.
3. During installation, **check the box** that says:

4. Verify installation:
```bash
python --version
```

🔹 macOS / Linux

Python 3 is often pre-installed. To verify:
```bash
python3 --version
```

If not installed:

macOS: Install via Homebrew
```bash
brew install python
```


2. Install PyCharm (Optional but Recommended)

PyCharm is a powerful IDE for Python development.

Download from: https://www.jetbrains.com/pycharm/download/

Choose the Community Edition (free) or Professional Edition.

Install and open PyCharm.

When prompted, configure your Python interpreter (the Python installation from Step 1).

# Email Group Sender

This Python project reads a list of email addresses from a CSV file, groups recipients from the same company (based on their email domain), and sends one email per company — placing all recipients in **BCC**.  

---

## 🚀 Features

- Reads email addresses from a CSV file  
- Groups recipients by company domain (e.g., `@example.com`)  
- Sends one email per company  
- Uses **BCC** to keep recipients private  
- Supports both plain text and HTML email content  

---

## 📋 Requirements

- Python 3.8 or later  
- A working SMTP account (e.g., Gmail, Outlook, etc.)  

---

## 🧩 Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/email-group-sender.git
   cd email-group-sender
```


2. **Create a virtual environment (recommended):**
```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
```

3. **Install dependencies:**

```bash
  pip install -r requirements.txt
```





## Execute

1. Update the recipients list in the recipients.csv file. Add a list of the recipients you want to send in the following 
   format.

```csv

NAME,EMAIL
company1,firstname.lastname@gmail.com
company2,firstname.lastname@gmail.com

```

2. Execute the Python code :

```bash
  python emailing.py
```

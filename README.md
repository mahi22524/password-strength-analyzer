# 🔒 Password Strength Analyzer

A Python-based web application built using **Streamlit** that analyzes password strength and helps users create more secure passwords. The application evaluates password complexity, detects password reuse using SQLite, securely stores password hashes with SHA-256, and suggests strong password alternatives.

---

## 📌 Project Overview

This project was developed as part of my internship to understand password security concepts and secure application development using Python.

The application checks password strength based on multiple security rules and encourages users to create stronger, more secure passwords.

---

## ✨ Features

- ✅ Password length validation
- ✅ Uppercase letter detection
- ✅ Lowercase letter detection
- ✅ Number detection
- ✅ Special character detection
- ✅ Password strength scoring
- ✅ Progress bar for security score
- ✅ Password improvement suggestions
- ✅ Strong password generator
- ✅ Show/Hide password option
- ✅ Password reuse detection using SQLite
- ✅ SHA-256 password hashing

---

## 🛠 Technologies Used

- Python
- Streamlit
- SQLite3
- hashlib (SHA-256)
- Regular Expressions (`re`)
- Git
- GitHub

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── app.py                 # Streamlit user interface
├── database.py            # SQLite database functions
├── utils.py               # Helper functions (hashing & password generation)
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore
├── assets/
└── passwords.db
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahi22524/password-strength-analyzer.git
```

### 2. Open the project

```bash
cd password-strength-analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

> Add screenshots after uploading them to the `assets` folder.

Example:

- Home Screen
- Weak Password Detection
- Strong Password Detection
- Password Reuse Detection

---

## 🔐 Security Concepts Used

- Password Complexity Validation
- SHA-256 Password Hashing
- Password Reuse Detection
- Secure Password Generation
- SQLite Database Storage

---

## 📈 Future Improvements

- Password entropy calculation
- Estimated password crack time
- Breached password detection using API
- Password history management
- Export password security report

---

## 👨‍💻 Author

**Bula Mahendra**

- GitHub: https://github.com/mahi22524
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ If you found this project useful, consider giving it a star!
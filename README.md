# 🔐 QR Code Based OTP Authentication (Python)

![Language](https://img.shields.io/badge/Language-Python-blue)
![Security](https://img.shields.io/badge/Security-TOTP-green)
![Library](https://img.shields.io/badge/Library-pyotp-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project implements a **secure authentication system using Time-Based One-Time Password (TOTP)**.

A QR code is generated for the user, which can be scanned using apps like **Google Authenticator**. The system then verifies OTPs in real-time for secure login.

---

## 🎯 Objectives

* Implement **2-Factor Authentication (2FA)**
* Generate secure OTP using TOTP algorithm
* Use QR codes for easy user setup
* Enhance login security

---

## 🚀 Features

* 🔑 Secret key generation
* 📷 QR code generation for authenticator apps
* ⏱️ Time-based OTP generation
* ✅ OTP verification system
* 🔐 Secure login validation

---

## 🧠 Concepts Used

* TOTP (Time-Based One-Time Password)
* Base32 encoding
* QR Code generation
* Authentication systems
* Python libraries

---

## 🛠️ Technologies Used

* Python
* `pyotp` → OTP generation
* `qrcode` → QR code creation

---

## 📂 Project Structure

```id="otp1"
otp_project.py
│
├── Generate Secret Key
├── Create QR Code
├── Generate OTP
└── Verify OTP
```

---

## ⚙️ How It Works

1. Generate a unique **secret key**
2. Create a **QR code** using the key
3. User scans QR using authenticator app
4. App generates OTP every 30 seconds
5. User enters OTP
6. System verifies OTP

---

## 🔄 Workflow

* Run program
* Scan QR code
* Get OTP from authenticator
* Enter OTP
* Verify login

---

## 💻 Installation & Setup

### 🔧 Requirements

* Python 3.x

### ▶️ Install Dependencies

```bash id="otp2"
pip install pyotp qrcode[pil]
```

### ▶️ Run the Program

```bash id="otp3"
python otp_project.py
```

---

## 🖥️ Sample Output

```id="otp4"
Secret Key: JBSWY3DPEHPK3PXP
QR code saved as qrcode.png
Current OTP: 123456

Enter OTP: 123456
Login successful ✅
```

---

## 📊 Core Code Snippets

### 🔑 Generate Secret

```python id="otp5"
secret = pyotp.random_base32()
```

### 📷 Generate QR Code

```python id="otp6"
uri = pyotp.totp.TOTP(secret).provisioning_uri(
    name="user@example.com",
    issuer_name="MyApp"
)
```

### 🔐 Verify OTP

```python id="otp7"
totp.verify(user_otp)
```

---

## ⚠️ Important Notes

* OTP changes every **30 seconds**
* QR code must be scanned once for setup
* Secret key should be kept secure
* Works with apps like:

  * Google Authenticator
  * Microsoft Authenticator

---

## 🔮 Future Enhancements

* 🌐 Web login system integration
* 🗄️ Database storage for users
* 📱 Mobile app integration
* 🔐 Multi-user authentication
* ⏳ Backup codes

---

## 🤝 Contribution

Feel free to fork and improve this project.

---

## 🛠️ Author

**Sri Man**
🔗 GitHub: https://github.com/Sriman-7

---

## 📄 License

Educational use only.

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!

---

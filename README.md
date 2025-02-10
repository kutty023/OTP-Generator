# 🔐 OTP Generation in Python

## 📌 Overview  
This project showcases different Python-based OTP generation methods, ranging from basic pseudo-random generators to secure cryptographic and time-based OTPs.

## Deployed Link : https://otp-generator-sgmd.onrender.com 

## 📜 How This Website Was Built  
### **📌 Technologies Used**
This OTP Generator was built using the following technologies:

|       **Technology**      |                **Purpose**                    |
|---------------------------|-----------------------------------------------|
| **Flask**                 | Backend server to handle OTP generation       |
| **Gunicorn**              | Production-ready WSGI server for hosting      |
| **PyOTP**                 | Library for time-based OTPs (TOTP)            |
| **HTML, CSS, JavaScript** | Frontend interface for user interaction       |
| **Fetch API (JS)**        | Sends POST requests to Flask API to get OTPs  |
| **Render**                | Deployment platform for hosting the Flask app |

## 📜 How It Was Deployed/hosted on Render  
Follow these steps to deploy the Flask OTP Generator on **Render**:

### Render (Best Free Option for Flask)
- ✅ Free & easy to deploy Flask + HTML, CSS, JS
- ✅ Supports Auto-Deploy from GitHub

### **1. 🚀 Quick Setup** 
```sh
    pip install gunicorn
    echo "web: gunicorn app:app" > Procfile
```

### **2. Create a `requirements.txt` File**
Ensure your project has a `requirements.txt` file listing the dependencies:
```txt
    flask
    pyotp
    gunicorn
```
### **3. Add a Procfile (For Deployment) if not present
Create a file named Procfile in your project root (without any extension) and add:
```txt
    web: gunicorn app:app
```
Why? gunicorn is a production-ready server for Flask apps.

### **4. Add files to git and Push them to GitHub**
```sh
    git add .
    git commit -m "Initial commit"
    git push
```
### **5. Deploy on Render**
- 1. Go to [Render](https://render.com) and sign in with GitHub.
- 2. Click "New Web Service".
- 3. Select your GitHub repository.
- 4. Choose Python 3.x as the runtime.
- 5. In the Build Command, enter:
```sh
    pip install -r requirements.txt
```
- 6. In the Start Command, enter:
```sh
    gunicorn app:app
```
- 7. Click Create Web Service and wait for deployment to complete.


## 📜 Methods of OTP Generation
### **1️⃣ PRNG-Based OTP (Pseudo-Random Number Generation)**
- **Method**: `random.randint()` / `random.choices()`
- **Use Case**: Quick OTPs, non-sensitive applications
- **Who Uses It?**: Small applications, testing environments
- **Security**: ❌ **Not secure** (predictable with enough samples)

### **2️⃣ Cryptographically Secure OTP**
- **Method**: `secrets.randbelow(10)`
- **Use Case**: Secure OTPs for sensitive applications
- **Who Uses It?**: Banks, secure login systems
- **Security**: ✅ Highly secure

### **3️⃣ Time-Based OTP (TOTP)**
- **Method**: `pyotp.TOTP()`
- **Use Case**: Two-Factor Authentication (2FA)
- **Who Uses It?**: Google Authenticator, banking apps, cybersecurity firms
- **Security**: ✅ Highly secure

### **4️⃣ Hash-Based OTP (HOTP-like)**
- **Method**: `hashlib.sha256()`
- **Use Case**: OTPs based on secrets and timestamps
- **Who Uses It?**: Secure systems, user authentication
- **Security**: ✅ Secure, but slower than TOTP

### **5️⃣ Alphanumeric OTPs**
- **Method**: `random.choices()` / `secrets.choice()`
- **Use Case**: OTPs with letters & numbers
- **Who Uses It?**: E-commerce, email verifications
- **Security**: ✅ Secure with `secrets`, ❌ Not secure with `random`

---

## 🚀 Best OTP Methods & Use Cases  
| Method                | Security         | Use Case                  | Who Uses It?                       |
|-----------------------|------------------|---------------------------|------------------------------------|
| `random.randint()`    | ❌ Not Secure    | Simple apps, testing     | Small projects                     |
| `secrets.randbelow()` | ✅ Secure        | Banking, authentication  | Banks, finance                     |
| `pyotp.TOTP()`        | ✅ Highly Secure | 2FA authentication       | Google Authenticator, Banking apps |
| `hashlib.sha256()`    | ✅ Secure        | Secure user verification | Security apps                      |
| `secrets.choice()`    | ✅ Secure        | Alphanumeric OTPs        | E-commerce, websites               |

---

## 📂 Project Setup
### **🔹 1. Install Dependencies**
```sh
    pip install -r requirements.txt
```

### **🔹 2. Run the Flask Server**
```sh
    python app.py
```
### **📌 The server will run at http://127.0.0.1:5000/.**

### **🔹 3. Open in Browser**
Go to: http://127.0.0.1:5000/

## 📜 Conclusion
✅ Best security: pyotp.TOTP() for 2FA
✅ Best for banking: secrets.randbelow()
✅ Best for websites: secrets.choice()
💡 For real-world security, avoid random.randint()!

## 📜 License
This project is open-source under the MIT License.


## 🌟 Contributions
Feel free to contribute, improve security, or add new OTP generation techniques! 🚀

## 🔗 Connect With Me
[LinkedIn](https://www.linkedin.com/in/arthi-r-aa41b5191/) 

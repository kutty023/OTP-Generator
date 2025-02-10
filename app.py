from flask import Flask, request, jsonify, render_template
import random
import string
import secrets
import pyotp
import hashlib
import time

app = Flask(__name__)

# using random.randint
def generateOTP():
    otp = random.randint(1000, 9999)
    return otp

# using random.choices and string.digits
def generate_otp(length=4):
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

# Secure OTP Generator (Using secrets module)
def generate_secure_otp(length=4):
    # secrets.randbelow(n) is a function from Python’s secrets module that generates a secure random integer between 0 and n-1.
    otp = ''.join(str(secrets.randbelow(10)) for i in range(length))
    return otp

# Time based otp generator
def time_based_otp_generator():
    totp = pyotp.TOTP(pyotp.random_base32(),digits = 4)
    return totp.now() # will generate a new OTP every 30 seconds0 

# Hash based OTP generator i.e., secret+timestamp
def generate_hashed_opt(secret = "my_secret_key", length=4):
    timestamp = str(int(time.time())) # get current timestamp
    hash_value = hashlib.sha256((secret+timestamp).encode()).hexdigest()
    # Extract only digits from the hash
    numeric_hash = ''.join(filter(str.isdigit, hash_value)) 
    return numeric_hash[:length] if len(numeric_hash) >= length else numeric_hash.ljust(length, '0')

#Generating Alphanumeric OTP
def generate_alphanumeric_otp(length=4):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))

#Generating Alphanumeric OTP using secrets module
def generate_secure_alphanumeric_otp(length=4):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# Mapping otp methods
otp_methods = {
    "otp1" : generateOTP,
    "otp2" : generate_otp,
    "otp3" : generate_secure_otp,
    "otp4" : time_based_otp_generator,
    "otp5" : generate_hashed_opt,
    "otp6" : generate_alphanumeric_otp,
    "otp7" : generate_secure_alphanumeric_otp
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_otp', methods=['POST'])
def generate_otp():
    data = request.json
    method = data.get('method')
    if method in otp_methods:
        otp = otp_methods[method]()
        return jsonify({"otp": otp})
    return jsonify({"error": "Invalid method"}), 400

if __name__ == '__main__':
    app.run(debug=True)
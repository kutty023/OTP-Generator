import random
import string
import secrets
import pyotp
import hashlib
import time

#  Using Pseudo-Random Number Generation (PRNG)

# using random.randint
def generateOTP():
    otp = random.randint(1000, 9999)
    return otp

otp1 = generateOTP()

# using string.digits
def generate_otp(length=4):
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

otp2 = generate_otp()

# Secure OTP Generator (Using secrets module)
def generate_secure_otp(length=4):
    # secrets.randbelow(n) is a function from Python’s secrets module that generates a secure random integer between 0 and n-1.
    otp = ''.join(str(secrets.randbelow(10)) for i in range(length))
    return otp

otp3 = generate_secure_otp()

print(f"OTP1 general using random integer: {otp1}", f"OTP2 general using random choice: {otp2}", f"OTP3 secure using secrets randbelow : {otp3}", sep='\n')

# Time based otp generator
def time_based_otp_generator():
    totp = pyotp.TOTP(pyotp.random_base32(),digits = 4)
    return totp.now()
otp4 = time_based_otp_generator()

print("OTP4 Time based OTP:", otp4)  # will generate a new OTP every 30 seconds0 

# Hash based OTP generator i.e., secret+timestamp

def generate_hashed_opt(secret = "my_secret_key", length=4):
    timestamp = str(int(time.time())) # get current timestamp
    hash_value = hashlib.sha256((secret+timestamp).encode()).hexdigest()
    # Extract only digits from the hash
    numeric_hash = ''.join(filter(str.isdigit, hash_value)) 
    return numeric_hash[:length] if len(numeric_hash) >= length else numeric_hash.ljust(length, '0')

otp5 = generate_hashed_opt()
print("OTP5 Hash based OTP:", otp5)  

#Generating Alphanumeric OTP

def generate_alphanumeric_otp(length=4):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))
otp6 = generate_alphanumeric_otp()
print("OTP6 Your alphanumeric OTP is:", otp6)


def generate_secure_alphanumeric_otp(length=4):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
otp7 = generate_secure_alphanumeric_otp()
print("OTP7 Your Secure alphanumeric OTP is:", otp7)
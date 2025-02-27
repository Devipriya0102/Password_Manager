import os
from cryptography.fernet import Fernet
KEY_PATH = os.path.join(os.path.dirname(__file__), "key.key")
# Generate and save key (Run this once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
     if not os.path.exists(KEY_PATH):
        raise FileNotFoundError(f"❌ ERROR: key.key not found in {KEY_PATH}")
     return open(KEY_PATH, "rb").read()
    

# Encrypt a password
def encrypt_password(password):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()

# Decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()  # Debugging print statement

if __name__=="__main__":
    generate_key()

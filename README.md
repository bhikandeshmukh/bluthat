# Bluetooth Jamming DoS Attack Script

This is a Python script designed to perform a Denial of Service (DoS) attack on Bluetooth devices by flooding them with L2CAP ping packets. The script is optimized for both **Termux (Android)** and **Linux** platforms.

## Features
- **Cross-Platform Support**: Works on Termux (Android) and Linux.
- **Stealth and Evasion**: Randomizes packet sizes and delays to avoid detection.
- **Advanced Targeting**: Scans for nearby Bluetooth devices.
- **Exploitation**: Placeholder for BlueBorne and other exploits.
- **Multi-Protocol Attacks**: Supports L2CAP, RFCOMM, and BLE attacks.
- **Self-Destruct Mechanism**: Deletes the script and traces if enabled.

## Prerequisites
- **Termux (Android)**:
  - Install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/).
  - Install the required tools:
    ```bash
    pkg update
    pkg install python
    pkg install termux-api
    pip install scapy
    ```
  - Grant Termux Bluetooth permissions:
    ```bash
    termux-bluetooth-enable
    ```

- **Linux**:
  - Install the required tools:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip bluez
    pip3 install scapy
    ```

## Installation
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/bhikandeshmukh/bluthat.git
   cd bluthat

## Usage

   #Run the script:
   ```bash
    python script.py

    Follow the on-screen prompts:

        Scan for nearby Bluetooth devices.

        Enter the target Bluetooth address.

        Specify the number of threads for the attack.

        Choose additional options (e.g., exploitation, self-destruct).

## Disclaimer

This script is for educational purposes only. Unauthorized use of this script to attack Bluetooth devices without permission is illegal and unethical. Always ensure you have explicit permission before testing or using such tools on any network or device.
License

This project is licensed under the MIT License. See the LICENSE file for details.



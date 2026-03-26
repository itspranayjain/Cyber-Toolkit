#!/usr/bin/env python3

from utils.banner import show_banner
from scanner.port_scanner import scan_ports
from password.checker import check_password
from integrity.file_checker import check_file


def main():
    show_banner()

    while True:
        print("""
================= MENU =================

1. Port Scanner
2. Password Checker
3. File Integrity Checker
4. Help
5. Exit

=======================================
""")

        choice = input("Select option >> ")

        # 🔎 PORT SCANNER
        if choice == "1":
            target = input("Target (IP/Domain) >> ")
            scan_ports(target)

        # 🔐 PASSWORD CHECKER
        elif choice == "2":
            password = input("Enter password >> ")
            check_password(password)

        # 📂 FILE INTEGRITY CHECKER
        elif choice == "3":
            file_path = input("Enter file path >> ")
            original_hash = input("Enter original hash >> ")
            check_file(file_path, original_hash)

        # 📖 HELP MENU
        elif choice == "4":
            print("""
============= HELP MENU =============

1. Port Scanner:
   - Enter a valid IP or domain
   - Example: 127.0.0.1
   - Example: scanme.nmap.org

2. Password Checker:
   - Enter any password
   - Tool will check strength

3. File Integrity Checker:
   - Enter file path (e.g., test.txt)
   - Enter original SHA256 hash

4. Help:
   - Shows this menu

5. Exit:
   - Close the tool

====================================
""")

        # ❌ EXIT
        elif choice == "5":
            print("Exiting Cyber Toolkit... 👋")
            break

        # ⚠️ INVALID INPUT
        else:
            print("Invalid option ❌ Try again.")


# 🚀 PROGRAM ENTRY
if __name__ == "__main__":
    main()

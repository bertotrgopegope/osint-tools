import os
import time
import sys
import subprocess

# Warna ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def typing_effect(text, color=WHITE, speed=0.02):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    clear_screen()
    # PASTIKAN PATH GAMBAR INI SESUAI
    image_path = "/storage/emulated/0/avg/bf9125b0db224b407f51641da46db42c.jpg"
    
    try:
        # Tampilkan gambar pake chafa (atur ukuran di sini)
        subprocess.run(["chafa", "--size=45x22", "--align=center", image_path])
    except FileNotFoundError:
        print("[!] Chafa belum terinstall. Ketik: pkg install chafa")
    except Exception as e:
        print(f"[!] Gagal nampilin gambar: {e}")

    print(f"{CYAN}    ======================================================{RESET}")
    print(f"{YELLOW}               [ OSINT TOOLKIT - TERMUX ]{RESET}")
    print(f"{CYAN}    ======================================================{RESET}")
    print(f"{WHITE}     Author: mr-robertooo | System: Android{RESET}\n")

def main_menu():
    banner()
    print(f"{GREEN}[1]{RESET} IP Geolocation Tracker")
    print(f"{GREEN}[2]{RESET} Google Dorking Tool")
    print(f"{GREEN}[3]{RESET} System Information")
    print(f"{RED}[0]{RESET} Exit\n")
    
    choice = input(f"{YELLOW}┌──({WHITE}root@termux{YELLOW})-[{WHITE}~{YELLOW}]\n└─$ {RESET}").strip()
    
    if choice == '1':
        typing_effect("[*] Menjalankan IP Tracker...", GREEN)
        time.sleep(1)
        os.system('python iptrack.py')
        input(f"\n{YELLOW}Tekan Enter buat balik ke menu...{RESET}")
        main_menu()
    elif choice == '2':
        typing_effect("[*] Menjalankan Dorking Tool...", GREEN)
        time.sleep(1)
        os.system('python dorker.py')
        input(f"\n{YELLOW}Tekan Enter buat balik ke menu...{RESET}")
        main_menu()
    elif choice == '3':
        typing_effect("[*] Mengambil info sistem...", GREEN)
        time.sleep(1)
        os.system('uname -a')
        input(f"\n{YELLOW}Tekan Enter buat balik ke menu...{RESET}")
        main_menu()
    elif choice == '0':
        typing_effect("[!] Keluar...", RED)
        sys.exit()
    else:
        typing_effect("[-] Perintah tidak dikenal.", RED)
        time.sleep(1)
        main_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Dihentikan oleh user.{RESET}")

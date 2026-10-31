import urllib.parse
import webbrowser
import os
import time
import sys

# Warna ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Daftar Dork (Ditambahin jadi 20)
DORKS = {
    "1": {"name": "Admin Login Pages", "query": 'inurl:admin intitle:login'},
    "2": {"name": "Exposed Config (.env)", "query": 'filetype:env "DB_PASSWORD"'},
    "3": {"name": "Exposed SQL Databases", "query": 'filetype:sql "INSERT INTO"'},
    "4": {"name": "Open Directory", "query": 'intitle:index.of "parent directory"'},
    "5": {"name": "WordPress Config Backup", "query": 'inurl:wp-config.php.bak'},
    "6": {"name": "PHP Info Leak", "query": 'intitle:"phpinfo()" filetype:php'},
    "7": {"name": "Exposed CCTV Cams", "query": 'inurl:"/view/index.shtml"'},
    "8": {"name": "API Keys Leak", "query": 'filetype:json "api_key"'},
    "9": {"name": "Password Files (TXT)", "query": 'filetype:txt intext:"password"'},
    "10": {"name": "PDF Confidential", "query": 'filetype:pdf "confidential"'},
    "11": {"name": "FTP Logins", "query": 'inurl:"ftp://" ext:txt'},
    "12": {"name": "SSH Private Keys", "query": 'filetype:pem "PRIVATE KEY"'},
    "13": {"name": "Exposed Docker Env", "query": 'filetype:yml "docker-compose"'},
    "14": {"name": "Backup Files (ZIP/RAR)", "query": 'intitle:index.of backup.zip OR backup.rar'},
    "15": {"name": "Subdomain Takeovers", "query": 'inurl:"cpanel" OR inurl:"webmail"'},
    "16": {"name": "Git Config Leak", "query": 'filetype:gitconfig "github"'},
    "17": {"name": "Swagger UI API", "query": 'inurl:"swagger-ui.html"'},
    "18": {"name": "Exposed Log Files", "query": 'filetype:log "error"'},
    "19": {"name": "Directory Listing (Parent)", "query": 'intitle:"index of /" "server at"'},
    "20": {"name": "Sensitive Docs (Gov)", "query": 'site:gov filetype:xlsx'}
}

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def typing_effect(text, color=WHITE, speed=0.01):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    clear_screen()
    print(f"{RED}    ======================================================{RESET}")
    print(f"{YELLOW}          [ GOOGLE DORKING AUTOMATOR - V2.0 ]{RESET}")
    print(f"{RED}    ======================================================{RESET}")
    print(f"{WHITE}     Author: mr-robertooo | Termux Edition{RESET}\n")

def show_menu():
    banner()
    print(f"{CYAN}Pilih Kategori Dork:{RESET}")
    print(f"{WHITE}-------------------------------------------------------{RESET}")
    
    # Nampilin menu 2 kolom biar rapi
    for i in range(1, 11):
        key1 = str(i)
        key2 = str(i + 10)
        name1 = DORKS[key1]['name']
        name2 = DORKS[key2]['name']
        print(f" {GREEN}[{key1:2}]{RESET} {name1:<25} {GREEN}[{key2:2}]{RESET} {name2}")
        
    print(f"{WHITE}-------------------------------------------------------{RESET}")
    print(f" {MAGENTA}[99]{RESET} Ketik Dork Manual")
    print(f" {RED}[0]{RESET}  Kembali / Keluar")
    print(f"{WHITE}======================================================={RESET}")

def jalankan_dork(query_name, query_string):
    target = input(f"\n{YELLOW}[?] Masukkan domain target (contoh: ui.ac.id / kosongkan buat global): {RESET}").strip()
    
    # Gabungin query
    final_query = f"{query_string} site:{target}" if target else query_string
    
    # Encode ke format URL
    encoded_query = urllib.parse.quote(final_query)
    url = f"https://www.google.com/search?q={encoded_query}"
    
    print(f"\n{GREEN}[+] Dork:{RESET} {query_name}")
    print(f"{GREEN}[+] Query:{RESET} {final_query}")
    typing_effect("[*] Membuka Google di browser...", CYAN)
    
    time.sleep(1)
    webbrowser.open(url) # Buka browser
    
    input(f"\n{YELLOW}Tekan Enter buat balik ke menu...{RESET}")

def main():
    while True:
        show_menu()
        choice = input(f"{YELLOW}┌──({WHITE}root@dorker{YELLOW})-[{WHITE}~{YELLOW}]\n└─$ {RESET}").strip()
        
        if choice == '0':
            typing_effect("[!] Keluar dari sistem...", RED)
            break
            
        elif choice == '99':
            print()
            custom_query = input(f"{YELLOW}[?] Masukkan query manual (misal: inurl:admin): {RESET}").strip()
            if custom_query:
                jalankan_dork("Manual Query", custom_query)
            
        elif choice in DORKS:
            dork = DORKS[choice]
            jalankan_dork(dork['name'], dork['query'])
            
        else:
            typing_effect("[-] Pilihan tidak valid. Masukkan angka 1-20.", RED)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Program dihentikan.{RESET}")	

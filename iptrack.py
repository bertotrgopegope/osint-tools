import requests
import sys
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def track_ip(ip_address):
    print(f"[*] Melacak IP: {ip_address}...")
    
    # API Endpoint (Gratis, tanpa API Key)
    url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print("\n" + "="*30)
            print(f"  INFORMASI IP: {ip_address}")
            print("="*30)
            print(f"  Negara    : {data.get('country')} ({data.get('countryCode')})")
            print(f"  Region    : {data.get('regionName')}")
            print(f"  Kota      : {data.get('city')}")
            print(f"  Zip Code  : {data.get('zip', '-')}")
            print(f"  ISP       : {data.get('isp')}")
            print(f"  Org       : {data.get('org', '-')}")
            print(f"  Timezone  : {data.get('timezone')}")
            print(f"  Latitude  : {data.get('lat')}")
            print(f"  Longitude : {data.get('lon')}")
            print(f"  Maps      : https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
            print("="*30 + "\n")
        else:
            print(f"[-] Gagal melacak IP: {data.get('message')}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error koneksi: {e}\n")
    except Exception as e:
        print(f"[-] Error: {e}\n")

def main():
    clear_screen()
    print("=== IP GEOLOCATION TRACKER ===")
    
    if len(sys.argv) > 1:
        track_ip(sys.argv[1])
    else:
        while True:
            ip_input = input("Masukkan IP target (atau ketik 'exit' buat keluar): ").strip()
            if ip_input.lower() == 'exit':
                break
            if ip_input:
                track_ip(ip_input)

if __name__ == "__main__":
    main()

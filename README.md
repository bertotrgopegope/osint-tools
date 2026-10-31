# OSINT Tools

Kumpulan tools berbasis Python untuk kebutuhan Open Source Intelligence (OSINT) ringan, dioptimalkan untuk Termux (Android).

## Tools Tersedia
- `menu.py` : Tampilan menu utama (menggunakan Chafa untuk background).
- `dorker.py` : Google Dorking otomatis (20 kategori).
- `iptrack.py` : IP Geolocation Tracker.

## Instalasi (Termux)

Buka Termux, lalu jalankan perintah berikut:

```bash
pkg update && pkg upgrade -y
pkg install python git chafa -y
pip install requests
```

Cara Pakai

1. Clone Repository
   ```bash
   git clone https://github.com/bertotrgopegope/osint-tools.git
   cd osint-tools
   ```
2. Jalankan Menu Utama
   ```bash
   python menu.py
   ```
3. **Jalankan Tool Tertentu (Langsung)**
   - Buka Dorker: `python dorker.py`
   - Buka IP Tracker: `python iptrack.py`

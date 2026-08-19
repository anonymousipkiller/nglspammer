import requests
import time
import random

def spam_ngl(username, pesan, jumlah, delay=1):
    for i in range(jumlah):
        try:
            device_id = f"android-{random.randint(100000, 999999)}"
            payload = {
                "username": username,
                "message": pesan,
                "deviceId": device_id,
                "gameSlug": ""
            }
            req = requests.post(
                "https://ngl.link/api/submit",
                json=payload,
                headers={
                    "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36"
                }
            )
            if req.status_code == 200:
                print(f"[+] {i+1}/{jumlah} terkirim")
            else:
                print(f"[-] {i+1}/{jumlah} gagal")
        except Exception as e:
            print(f"[!] {i+1}/{jumlah} error: {e}")
        time.sleep(delay)

if __name__ == "__main__":
    username = input("Username target: ")
    pesan = input("Pesan spam: ")
    jumlah = int(input("Jumlah kirim: "))
    delay = float(input("Delay (detik, contoh 0.5): "))
    spam_ngl(username, pesan, jumlah, delay)

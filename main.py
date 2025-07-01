import requests
import random
import string
import base64
import time
import threading
import os
from queue import Queue

# === Config ===
THREADS = 10
RETRY_LIMIT = 2
BATCH_SIZE = 1000

# === Load Proxies ===
def load_proxies():
    proxies = []
    if os.path.exists("proxy.txt"):
        with open("proxy.txt") as f:
            proxies = [line.strip() for line in f if line.strip()]
    return proxies

def get_random_proxy(proxies):
    if not proxies:
        return None
    raw = random.choice(proxies)
    return {"http": raw, "https": raw}

# === Random Generators ===
def random_string(min_len=3, max_len=8):
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(min_len, max_len))).capitalize()

def random_name():
    return random_string(), random_string()

def random_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@airdropscriptfa.com"

def decode_ref(b64):
    try:
        return base64.b64decode(b64).decode().strip()
    except:
        return None

# === Registration Task ===
def register_task(ref_code, queue, proxies):
    while not queue.empty():
        try:
            _ = queue.get_nowait()
        except:
            return

        proxy = get_random_proxy(proxies)
        session = requests.Session()
        if proxy:
            session.proxies.update(proxy)

        ref_url = f"https://aetheris.company/register?ref={ref_code}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "text/html,application/xhtml+xml,application/xml",
        }

        try:
            session.get(ref_url, headers=headers, timeout=10)
        except:
            print("❌ Failed to load referral page.")
            return

        first, last = random_name()
        email = random_email()

        payload = {
            "email": email,
            "first": first,
            "last": last,
            "password": "123456",
            "password2": "123456",
            "ref": ref_code
        }

        headers.update({
            "Origin": "https://aetheris.company",
            "Referer": ref_url,
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

        for _ in range(RETRY_LIMIT):
            try:
                res = session.post("https://aetheris.company/api/reg", headers=headers, json=payload, timeout=15)
                if res.status_code == 200 and "token" in res.json():
                    print(f"✅ Registered: {email}")
                    return
            except:
                continue

        print(f"❌ Skipped: {email}")

# === Batch Runner ===
def run_batch(ref_code, count, proxies):
    queue = Queue()
    for _ in range(count):
        queue.put(1)

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=register_task, args=(ref_code, queue, proxies))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

# === Banner ===
def banner():
    print("\n" + "="*50)
    print("🌲 FOREST ARMY — Referral Booster Engine")
    print("📺 YouTube: https://youtube.com/forestarmy")
    print("📢 Telegram: https://t.me/forestarmy")
    print("="*50 + "\n")

# === Main ===
if __name__ == "__main__":
    banner()

    try:
        with open("code.txt") as f:
            codes = [decode_ref(line.strip()) for line in f if line.strip()]
            codes = [c for c in codes if c]
    except:
        print("❌ code.txt not found.")
        exit()

    try:
        total_count = int(input("🔢 Total referrals per code? "))
    except:
        print("❌ Invalid input.")
        exit()

    PROXIES = load_proxies()
    print(f"🔌 Proxy Mode: {'ON' if PROXIES else 'OFF'}")

    for code in codes:
        print(f"\n🚀 Starting referrals for decoded code: {code}")
        done = 0
        batch_num = 1
        while done < total_count:
            remaining = total_count - done
            batch_size = min(BATCH_SIZE, remaining)
            print(f"\n⚙️ Batch #{batch_num} — {batch_size} referrals")
            run_batch(code, batch_size, PROXIES)
            done += batch_size
            batch_num += 1
            time.sleep(1)

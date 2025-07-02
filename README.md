# itsmesatyavir - Aetheris Referral Automation Bot

Automates referral submissions for the [Aetheris](https://aetheris.xyz) platform using rotating proxies and infinite execution.

---

## 📌 Description

This script helps automate the referral process for Aetheris testnet or campaigns. It loops infinitely through referral codes, optionally using rotating proxies, and submits them to the endpoint. No manual input required after start.

---

## 📁 Project Structure

```
.
├── main.py         # Core automation script
├── code.txt        # List of referral codes or tokens
├── proxy.txt       # Optional: rotating proxy list
├── README.md       # Project documentation
└── LICENSE         # MIT License
```

---

## ⚙️ Features

- ✅ **Auto-run**: Starts automatically with no prompt
- 🔁 **Infinite loop**: Keeps submitting until manually stopped
- 🌍 **Rotating Proxies**: Supports `http`, `socks4`, `socks5`
- 🔐 **Token-based submission**: Securely reads from `code.txt`
- 💬 **Telegram Support** *(optional)*: Can be integrated for live updates
- 🧠 **Optimized for speed and reliability**

---

## 🧪 Requirements

Install Python 3.8+ and dependencies:

```bash
pip install aiohttp requests pysocks
```

---

## 📥 Usage

Clone the Repo
```bash
git clone https://github.com/itsmesatyavir/aetheris.git
cd aetheris
```

Run the script with:

```bash
python main.py
```

The script will:
- Load codes from `code.txt`
- Optionally use proxies from `proxy.txt`
- Submit each referral in a loop
- Rotate proxies per submission
- Run infinitely until you manually stop it (`CTRL+C`)

---

## 📄 Input File Formats

### `code.txt`  
Put one referral code or token per line:

```
MTY2NjQzMQ==
MTY2NjYyNg==
...
```

### `proxy.txt` *(optional)*  
Supports formats like:

```
http://username:password@ip:port
socks4://ip:port
socks5://user:pass@ip:port
```

If no proxies are given, script runs without proxy.

---

## 📬 Telegram Integration (Optional)

To enable Telegram updates:
1. Add your bot token and chat ID in the script.
2. Enable periodic `send_message()` updates to track progress.

---

## 📝 Example Output (Console)

```
Loaded 25 referral codes
Loaded 10 proxies
[✓] Submitted code: abc123xyz456
[✓] Submitted code: ref789token321 via Proxy - yes - (Germany)
[INFO] Sleeping 5 seconds before next round...
```

---

## 🧾 License

This project is licensed under the MIT License.

---

## 👤 Author

**itsmesatyavir**  
📺 YouTube: [Forest Army](https://www.youtube.com/forestarmy)  
📢 Telegram: [@forestarmy](https://t.me/forestarmy)

---

## 🌱 Stay Updated

Follow for future tool releases, guides, and validator scripts for Web3 projects.

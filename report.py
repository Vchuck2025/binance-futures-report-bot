import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS", "").split(",")
MESSAGE = "Binance Futures Report Bot 每小時自動推送測試成功 ✅"

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    for chat_id in CHAT_IDS:
        send_telegram_message(chat_id, MESSAGE)
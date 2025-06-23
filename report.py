import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS").split(",")

report_message = "✅ Binance Futures 自動報告已觸發並成功運行！"

def send_telegram_message(text):
    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": text})

send_telegram_message(report_message)

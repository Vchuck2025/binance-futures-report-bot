import os
import requests

# 從 GitHub Secrets 取得環境變數
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS")

# 驗證變數是否成功取得
print("✅ 開始執行 Binance Futures Report Bot")
print(f"🔐 BOT_TOKEN 長度：{len(BOT_TOKEN) if BOT_TOKEN else '未設定'}")
print(f"🆔 CHAT_IDS：{CHAT_IDS}")

# 建立訊息
message = "🚀 Binance Futures Report Bot 已成功觸發！"

# 發送到所有 chat_id
if BOT_TOKEN and CHAT_IDS:
    for chat_id in CHAT_IDS.split(","):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id.strip(),
            "text": message,
        }
        response = requests.post(url, data=payload)
        print(f"📬 發送至 {chat_id.strip()} - 狀態碼: {response.status_code}")
else:
    print("⚠️ 尚未設定 BOT_TOKEN 或 CHAT_IDS")

import requests
import json
import os

# 設定 Telegram
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_IDS = json.loads(os.environ.get("CHAT_IDS", "[]"))

# Binance Futures 合約價格 API（BTC、ETH、XRP、CRV）
symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "CRVUSDT"]
binance_url = "https://fapi.binance.com/fapi/v1/ticker/price"

# DefiLlama API 抓 TVL
def fetch_tvl():
    try:
        response = requests.get("https://api.llama.fi/tvl")
        if response.status_code == 200:
            data = response.json()
            return f"TVL: ${data['tvl']:,}"
        else:
            return "TVL: 無法獲取"
    except:
        return "TVL: 發生錯誤"

# Binance 合約價格
def fetch_prices():
    prices = []
    for symbol in symbols:
        try:
            res = requests.get(f"{binance_url}?symbol={symbol}")
            data = res.json()
            prices.append(f"{symbol}: ${float(data['price']):,.2f}")
        except:
            prices.append(f"{symbol}: 無資料")
    return "\n".join(prices)

# 傳送到 Telegram
def send_report():
    tvl = fetch_tvl()
    prices = fetch_prices()
    message = f"📊 Binance 合約報告\n\n{prices}\n\n{tvl}"

    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        try:
            requests.post(url, data=payload)
        except:
            print(f"❌ 傳送給 {chat_id} 失敗")

# 執行
if __name__ == "__main__":
    send_report()

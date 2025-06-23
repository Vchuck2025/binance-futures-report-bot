# Binance Futures Report Bot

每小時自動推送 Binance 報告至 Telegram 的 GitHub Actions 專案。

## 使用方式
1. 上傳 `report.py` 到你的 repository。
2. 建立 `.github/workflows/report.yml`。
3. 設定 Repository Secrets：`BOT_TOKEN`、`CHAT_IDS`。
4. GitHub Actions 將每小時自動執行並推送訊息。

## Secrets 設定
- `BOT_TOKEN`: 你的 Telegram Bot Token
- `CHAT_IDS`: 接收訊息的用戶 ID，使用逗號分隔（例如：123456789,987654321）

## 測試訊息
執行後訊息範例：`Binance Futures Report Bot 每小時自動推送測試成功 ✅`
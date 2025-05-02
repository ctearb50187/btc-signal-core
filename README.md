# BTC Event Bot Optimized v2.1

## ✅ 功能特色

- 支援 TradingView Webhook 觸發自動下注
- 自動推播訊號到 Telegram
- 使用 SQLite 紀錄所有訊號紀錄（內建模組）

## 🚀 快速啟動

1. 安裝依賴
```
pip install -r requirements.txt
```

2. 啟動伺服器
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## 🔗 TradingView Webhook 設定

Webhook URL:
```
https://你的-render-url.onrender.com/webhook
```

JSON Payload 範例：
```json
{
  "strategy": {
    "order_action": "buy"
  }
}
```

## ✅ Render Start Command

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
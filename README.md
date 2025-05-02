# BTC Event Bot PRO v2

## 功能亮點

- Webhook 事件接收
- 自動下注 Binance 合約（模擬邏輯）
- Telegram 推播訊號
- SQLite 紀錄訊號歷史

## 啟動方式

```
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## TradingView Webhook JSON 範例

```json
{
  "strategy": {
    "order_action": "buy"
  }
}
```

## Render 設定

Start Command:
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
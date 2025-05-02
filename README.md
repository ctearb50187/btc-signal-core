# BTC 事件合約自動下注系統（穩定版 SDK）

## 啟動方式

1. 安裝依賴
```
pip install -r requirements.txt
```

2. 啟動伺服器
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

3. TradingView Webhook 設定範例
```json
{
  "strategy": {
    "order_action": "buy"
  }
}
```

4. Render 設定
- Python 環境
- Build command 留空
- Start command 設為：
```
uvicorn main:app --host 0.0.0.0 --port 10000
```
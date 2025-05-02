# BTC 事件合約自動下注系統

## 快速啟動

1. 安裝依賴
```
pip install -r requirements.txt
```

2. 啟動伺服器
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

3. TradingView Webhook 設定
```
URL: https://你的Render網址/webhook
JSON:
{
  "strategy": {
    "order_action": "buy"  # 或 "sell"
  }
}
```

4. Render 部署方式：
- 使用 GitHub 推送此專案
- 在 Render 新增 Web Service，指向 `main:app`
- 選擇 Python 環境、Auto deploy、Build command 留空、Start command 設為：
```
uvicorn main:app --host 0.0.0.0 --port 10000
```
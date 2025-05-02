from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import asyncio
import os
import sqlite3
from binance_client import place_event_bet
from telegram_bot import send_telegram_alert
from logger import log_action

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <html>
        <head>
            <title>BTC Signal Core</title>
            <style>
                body { font-family: Arial; text-align: center; padding: 50px; }
                h1 { color: #0096FF; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>🚀 BTC Signal Core</h1>
            <p>你的訊號中樞已啟動！</p>
            <p>此應用專為 Binance 事件合約而設計，並支援 TradingView Webhook、Telegram 推播與 SQLite 記錄。</p>
            <p><a href='/history'>查看訊號紀錄</a></p>
        </body>
    </html>
    """

@app.get("/history", response_class=HTMLResponse)
async def history():
    db_path = os.path.join(os.path.dirname(__file__), "signals.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS actions (timestamp TEXT, action TEXT)")
    records = cursor.execute("SELECT timestamp, action FROM actions ORDER BY timestamp DESC").fetchall()
    conn.close()

    rows = "".join(f"<tr><td>{t}</td><td>{a}</td></tr>" for t, a in records)
    return f"""
    <html>
        <head>
            <title>歷史訊號 - BTC Signal Core</title>
            <style>
                body {{ font-family: Arial; padding: 20px; }}
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>📜 歷史訊號紀錄</h1>
            <table>
                <tr><th>時間</th><th>方向</th></tr>
                {rows}
            </table>
            <br><a href="/">⬅ 回首頁</a>
        </body>
    </html>
    """

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    signal = data.get("strategy", {}).get("order_action", "none")

    if signal in ["buy", "sell"]:
        asyncio.create_task(place_event_bet(signal))
        send_telegram_alert(f"📢 Webhook 訊號接收：{signal.upper()}")
        log_action(signal)
    return {"status": "ok", "action": signal}
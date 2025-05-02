from fastapi import FastAPI, Request
import asyncio
from binance_client import place_event_bet
from telegram_bot import send_telegram_alert
from logger import log_action

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    signal = data.get("strategy", {}).get("order_action", "none")

    if signal in ["buy", "sell"]:
        asyncio.create_task(place_event_bet(signal))
        send_telegram_alert(f"📢 Webhook 訊號接收：{signal.upper()}")
        log_action(signal)
    return {"status": "ok", "action": signal}
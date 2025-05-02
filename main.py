from fastapi import FastAPI, Request
import asyncio
from binance_client import place_event_bet

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    signal = data.get("strategy", {}).get("order_action", "none")

    if signal in ["buy", "sell"]:
        asyncio.create_task(place_event_bet(signal))
    return {"status": "ok"}
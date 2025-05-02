from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK", "message": "BTC Event Signal Core is live."}

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    return {
        "status": "received",
        "data": payload
    }

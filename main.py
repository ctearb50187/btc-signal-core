from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.post("/ai_predict")
async def ai_predict(data: dict):
    # 模擬 AI 預測結果
    open_price = data.get("open", 0)
    close_price = data.get("close", 0)
    direction = "buy" if close_price > open_price else "sell" if close_price < open_price else "hold"
    confidence = 0.87 if direction != "hold" else 0.5
    return {"prediction": direction, "confidence": confidence}
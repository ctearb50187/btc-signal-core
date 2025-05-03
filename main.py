from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

try:
    model = joblib.load("xgb_btc_direction_model.pkl")
except:
    model = None

@app.post("/ai_predict")
async def ai_predict(data: dict):
    open_p = data.get("open", 0)
    high = data.get("high", 0)
    low = data.get("low", 0)
    close = data.get("close", 0)
    features = np.array([[open_p, high, low, close]])
    if model and hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0]
        direction_idx = int(np.argmax(proba))
        prediction = ["buy", "sell", "hold"][direction_idx]
        confidence = float(proba[direction_idx])
    else:
        prediction = "buy" if close > open_p else "sell" if close < open_p else "hold"
        confidence = 0.87 if prediction != "hold" else 0.5
    return {"prediction": prediction, "confidence": confidence}
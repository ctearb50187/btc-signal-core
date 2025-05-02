from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.trend import MACD, SMAIndicator
from ta.volatility import BollingerBands

app = FastAPI()
model = joblib.load("xgb_btc_direction_model.pkl")

@app.get("/ai_predict")
def ai_predict(open: float, high: float, low: float, close: float):
    # Construct one-row DataFrame
    data = pd.DataFrame([{
        "open": open,
        "high": high,
        "low": low,
        "close": close
    }])

    # Compute technical indicators
    data["rsi"] = RSIIndicator(close=data["close"]).rsi()
    data["macd"] = MACD(close=data["close"]).macd_diff()
    data["sma"] = SMAIndicator(close=data["close"], window=20).sma_indicator()
    bb = BollingerBands(close=data["close"])
    data["bb_bbm"] = bb.bollinger_mavg()
    data["bb_bbh"] = bb.bollinger_hband()
    data["bb_bbl"] = bb.bollinger_lband()
    stoch = StochasticOscillator(high=data["high"], low=data["low"], close=data["close"])
    data["stoch_k"] = stoch.stoch()
    data["stoch_d"] = stoch.stoch_signal()

    # Drop NA and predict
    data.dropna(inplace=True)
    if data.empty:
        return JSONResponse({"error": "Insufficient data for indicators"}, status_code=400)

    features = ["rsi", "macd", "sma", "bb_bbm", "bb_bbh", "bb_bbl", "stoch_k", "stoch_d"]
    prediction = model.predict(data[features])[0]
    label_map = {0: "buy", 1: "sell", 2: "hold"}
    return {"prediction": label_map[prediction]}
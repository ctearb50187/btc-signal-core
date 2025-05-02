
from fastapi import FastAPI, Request
import joblib
import pandas as pd

app = FastAPI()
model = None

@app.on_event("startup")
def load_model():
    global model
    model = "DUMMY_MODEL"

@app.post("/ai_predict")
async def ai_predict(request: Request):
    data = await request.json()
    return {"prediction": "buy"}  # placeholder response

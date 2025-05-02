
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def homepage():
    return FileResponse("index.html")

@app.post("/ai_predict")
async def ai_predict(request: Request):
    data = await request.json()
    return {"prediction": "buy"}  # 模擬回傳值，後續可替換為 AI 引擎

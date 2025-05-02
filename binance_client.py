from binance.client import Client

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
client = Client(api_key, api_secret)

def place_event_bet(direction):
    if direction == "buy":
        print("下注：BTC 將上漲")
        # 這裡可以加上 binance 下單邏輯
    elif direction == "sell":
        print("下注：BTC 將下跌")
        # 同上
from binance.client import Client

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
client = Client(api_key, api_secret)

def place_event_bet(direction):
    print(f"自動下注方向：{direction.upper()}")
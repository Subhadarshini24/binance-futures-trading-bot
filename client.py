from binance.client import Client

# API Keys
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"

# Binance Client
client = Client(api_key, api_secret)

# Futures Testnet
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
client.TIME_OFFSET = 1000
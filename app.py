import streamlit as st
from binance.client import Client
import logging

# API Keys
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"

# Binance Client
client = Client(api_key, api_secret)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
client.TIME_OFFSET = 1000

# Logging
logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# UI Title
st.title("📈 Binance Futures Trading Bot")

st.write("Place MARKET, LIMIT and STOP orders on Binance Futures Testnet")

# Inputs
symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001
)

price = None
stop_price = None

# LIMIT Inputs
if order_type == "LIMIT":

    price = st.number_input(
        "Price",
        min_value=1.0,
        value=84000.0
    )

# STOP Inputs
if order_type == "STOP":

    price = st.number_input(
        "Limit Price",
        min_value=1.0,
        value=84000.0
    )

    stop_price = st.number_input(
        "Stop Price",
        min_value=1.0,
        value=84100.0
    )

# Button
if st.button("Place Order"):

    try:

        order_data = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # LIMIT Order
        if order_type == "LIMIT":
            order_data["price"] = price
            order_data["timeInForce"] = "GTC"

        # STOP Order
        if order_type == "STOP":
            order_data["price"] = price
            order_data["stopPrice"] = stop_price
            order_data["timeInForce"] = "GTC"

        logging.info(f"Order Request: {order_data}")

        response = client.futures_create_order(**order_data)

        logging.info(f"Order Response: {response}")

        st.success("✅ Order Placed Successfully!")

        st.write("### Order Details")
        st.write(f"Order ID: {response['orderId']}")
        st.write(f"Symbol: {response['symbol']}")
        st.write(f"Type: {response['type']}")
        st.write(f"Side: {response['side']}")
        st.write(f"Status: {response['status']}")

    except Exception as e:

        logging.error(f"Error: {e}")

        st.error(f"❌ Error: {e}")
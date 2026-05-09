from client import client
import logging

# Logging Setup
logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def place_order(order_data):

    try:

        logging.info(f"Order Request: {order_data}")

        response = client.futures_create_order(**order_data)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:

        logging.error(f"Error: {e}")

        return str(e)
import argparse
from orders import place_order

# CLI Arguments
parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)
parser.add_argument("--stopprice", type=float)

args = parser.parse_args()

# Validation
if args.side.upper() not in ["BUY", "SELL"]:
    print("❌ Invalid side. Please use BUY or SELL.")
    exit()

if args.type.upper() not in ["MARKET", "LIMIT", "STOP"]:
    print("❌ Invalid order type. Use MARKET, LIMIT or STOP.")
    exit()

if args.quantity <= 0:
    print("❌ Quantity must be greater than 0.")
    exit()

if args.type.upper() == "LIMIT" and not args.price:
    print("❌ LIMIT orders require --price.")
    exit()

if args.type.upper() == "STOP" and (not args.price or not args.stopprice):
    print("❌ STOP orders require --price and --stopprice.")
    exit()

# Order Data
order_data = {
    "symbol": args.symbol,
    "side": args.side.upper(),
    "type": args.type.upper(),
    "quantity": args.quantity
}

# LIMIT Order
if args.type.upper() == "LIMIT":
    order_data["price"] = args.price
    order_data["timeInForce"] = "GTC"

# STOP Order
if args.type.upper() == "STOP":
    order_data["price"] = args.price
    order_data["stopPrice"] = args.stopprice
    order_data["timeInForce"] = "GTC"

# Place Order
response = place_order(order_data)

# Output
if isinstance(response, dict):

    print("\n✅ Order Placed Successfully!")

    print(f"Order ID: {response.get('orderId', 'N/A')}")
    print(f"Symbol: {response.get('symbol', 'N/A')}")
    print(f"Order Type: {response.get('type', 'N/A')}")
    print(f"Side: {response.get('side', 'N/A')}")
    print(f"Status: {response.get('status', 'N/A')}")

else:

    print(f"❌ Error: {response}")

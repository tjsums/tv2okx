import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# OKX API credentials from environment variables
OKX_API_KEY = os.getenv("OKX_API_KEY")
OKX_API_SECRET = os.getenv("OKX_API_SECRET")
OKX_PASS = os.getenv("OKX_PASS")
TRADINGVIEW_SECRET = os.getenv("TRADINGVIEW_SECRET")  # Secret to verify webhook source

@app.route('/webhook', methods=['POST'])
def webhook():
    # Validate secret
    secret = request.headers.get('X-Secret', '')
    if secret != TRADINGVIEW_SECRET:
        return jsonify({"error": "Unauthorized"}), 401

    # Process TradingView payload
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    try:
        # Example of extracting order details
        symbol = data.get("symbol")
        side = data.get("side")
        quantity = data.get("quantity")

        # Placeholder for sending orders to OKX
        response = send_order_to_okx(symbol, side, quantity)
        return jsonify({"status": "success", "response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def send_order_to_okx(symbol, side, quantity):
    """
    Function to send an order to OKX API
    This is a placeholder and should be replaced with the actual OKX API logic
    """
    # Example logic for sending orders to OKX
    order = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity
    }
    # You would use OKX's API here
    return {"message": "Order sent to OKX", "order": order}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
import requests
import json
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/Process',methods=['POST'])
def func():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Access individual parameters from the JSON
    param1 = data.get('channel')
    param2 = data.get('upiid')
    param3 = data.get('paymentmode')
    param4 = data.get('orderid')
    param5 = data.get('amount')

    # Example processing
    if not param1 or not param2 or not param3 or not param4 or not param5:
        return jsonify({"error": "Missing parameters"}), 400

    # Example response

    url = "https://sandbox.cashfree.com/pg/orders/sessions"
    body = {
        "payment_method": {
            "upi": {
                "channel": param1,
                "upi_id": param2,
                "upi_redirect_url": True,
                "upi_expiry_minutes": 10
            }
        },
        "payment_session_id": "session_dbsZETKGl2MIqM9x12CM_yuIsCshv4ABJladS3eE5t8QabuAKTClOytp5L_PAEkCP-9kwKFp1lE6NIcSIenA6hC7dK2gP1jcFH_maDDvd_Fm"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-version": "2023-08-01",
        "x-client-id": "TEST425000f78db163221d221dbd07000524",
        "x-client-secret": "TESTd020dacb6239e76cd735c41e9f460f5119616c81"
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()

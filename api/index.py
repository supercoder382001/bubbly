# import requests
# import json
import json

from flask import Flask,request,jsonify
# from initiate import initiate_
# from processorder import process_
# from validatevpa import validate_

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/create',methods=['POST'])
def create():
    data = {
        "message": True,
        "url": "ABC"
    }
    return data.json


@app.route('/Process',methods=['POST'])
def process():
    data = {
        "message": True,
        "url": "ABC"
    }
    return data

@app.route('/Validate',methods=['POST'])
def validate():
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Access individual parameters from the JSON
    param4 = data.get('orderid')
    param5 = data.get('upiid')
    # Example processing
    if not param4 or not param5:
        return jsonify({"error": "Missing parameters"}), 400


    res = {
        "message": True,
        "url": "ABC"
    }
    return json.dumps(res)

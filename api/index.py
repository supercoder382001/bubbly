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

@app.route('/Validate',methods=['GET'])
def validate():
    data = {
        "message": True,
        "url": "ABC"
    }
    return json.dumps(data)

# import requests
# import json
from flask import Flask,request,jsonify
from initiate import initiate_
from processorder import process_
from validatevpa import validate_
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

# @app.route('/create',methods=['POST'])
# def create():
#     return initiate_()

@app.route('/Process',methods=['POST'])
def process():
    return process_()

# @app.route('/Validate',methods=['GET'])
# def validate():
#     return validate_()

# import requests
# import json
import json
import importlib
import sys
from flask import Flask,request,jsonify
# from initiate import initiate_
# from processorder import process_
# from validatevpa import validate_
from os.path import dirname, abspath, join
current_dir = dirname(abspath(__file__))
initiate_path = join(current_dir, 'processorder.py.py')
spec = importlib.util.spec_from_file_location("initiate", initiate_path)
initiate = importlib.util.module_from_spec(spec)
sys.modules["initiate"] = initiate
spec.loader.exec_module(initiate)
result=initiate.process_()

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
    dir=dirname(abspath())
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
    return result

import requests
import json
from flask import jsonify


base = "http://127.0.0.1:5000/"
respone = requests.get(base, json= {'message': 'hello'})
text = respone.text
text = text[0]
print(text)
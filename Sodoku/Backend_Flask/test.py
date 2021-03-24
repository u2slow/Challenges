import requests


base = "http://127.0.0.1:5000/"
respone = requests.get(base)
print(respone)
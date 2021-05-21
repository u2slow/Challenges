import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/16/"
URLsolution = "https://cc.the-morpheus.de/solutions/16/"

resp = requests.get(URLchallenge).json()['list']

def solve(resp):
    print(resp)

print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)
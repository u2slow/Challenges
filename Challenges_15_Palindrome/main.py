import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/14/"
URLsolution = "https://cc.the-morpheus.de/solutions/14/"

def solve(resp):
    print(resp)
    return 1

resp = requests.get(URLchallenge).json()['list']
print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)
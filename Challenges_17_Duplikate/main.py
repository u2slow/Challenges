import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/17/"
URLsolution = "https://cc.the-morpheus.de/solutions/17/"

resp = requests.get(URLchallenge).json()['list']

def solve(resp):
    s = set(resp)
    if len(s) == len(resp):
        return False
    return True


for i in range(50):   
    resp = requests.get(URLchallenge).json()['list']
    print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)
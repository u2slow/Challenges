import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/18/"
URLsolution = "https://cc.the-morpheus.de/solutions/18/"

resp = requests.get(URLchallenge).json()['list']

def solve(resp):
    s = set(resp)
    for i in resp:
        r = 1
        while r <= 8:
            if i+r in s or i-r in s:
                return True
            r +=1
    return False


for i in range(50):
    resp = requests.get(URLchallenge).json()['list']
    print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)
import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/16/"
URLsolution = "https://cc.the-morpheus.de/solutions/16/"

resp = requests.get(URLchallenge).json()['list']

def solve(resp):
    resp.sort()
    sol = 1
    val = 1
    for i in range(len(resp)-1):
        if resp[i] == resp[i+1]-1:
            val = val +1 
            if val > sol:
                sol = val
        elif resp[i] == resp[i+1]:
            pass
        else:
            val = 1
    return sol
for i in range(50):
    resp = requests.get(URLchallenge).json()['list']
    print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)
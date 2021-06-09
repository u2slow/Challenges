import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/16/"
URLsolution = "https://cc.the-morpheus.de/solutions/16/"

resp = requests.get(URLchallenge).json()['list']

def solve(resp):
    sol = 0
    ran = 0
    for i in range(len(resp)-1):
        if resp[i] == resp[i+1]-1:
            ran = ran + 1
            if ran > sol:
                sol = ran
        else: ran = 0
    print(resp)
    print(sol)
    return 0


print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)

import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/15/"
URLsolution = "https://cc.the-morpheus.de/solutions/15/"

resp = requests.get(URLchallenge).json()['word']

def solve(resp):
    data = ""
    resp = resp.strip("/n")
    for i in resp:
        if i == " " or i == "'" or i == "," or i == "." or i == "!" or i == "?" or i == "-" or i == '"' or i == ":" or i == ";" or i == "/":
            continue
        data = data + i

    data = data[0:len(data)-1]
    i = len(data)-1
    redata = ""
    while i >= 0:
        redata = redata + data[i]
        i = i -1
    
    redata = redata.lower()
    data = data.lower()

    if redata == data:
        return True
    return False

for i in range(10):
    resp = requests.get(URLchallenge).json()['word']
    print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})).text)
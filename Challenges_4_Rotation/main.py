import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/4/"
URLsolution = "https://cc.the-morpheus.de/solutions/4/"

resp = requests.get(URLchallenge).json()

data = resp["list"]
k = resp["k"]%len(data)

data1 = data[:-k]
data2 = data[-k:]
data = data2 + data1


data = json.dumps({"token": data})

print(requests.post(URLsolution,data=data).text)
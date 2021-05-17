import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/7/"
URLsolution = "https://cc.the-morpheus.de/solutions/7/"

resp = requests.get(URLchallenge).json()

k = resp['k']
data = resp['list']

def solve():
    for i in range(len(data)):
        search = k - data[i]
        for n in range(len(data)):
            if data[n] == search:
                return [i,n]


print(k)
s = solve()
index1 = s[0]
index2 = s[1]
print(data[index1], data[index2])

print(requests.post(URLsolution, data = json.dumps({"token": solve()})).text)
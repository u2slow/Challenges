import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/8/"
URLsolution = "https://cc.the-morpheus.de/solutions/8/"

resp = requests.get(URLchallenge).json()

k = resp['k']
data = resp['list']

def solve():
    for i in data:
        for j in data:
            for m in data:
                for l in data:
                    if i + j + m + l == k:
                        return [data.index(i), data.index(j), data.index(m), data.index(l)]


print(k)
s = solve()
index1 = s[0]
index2 = s[1]
index3 = s[2]
index4 = s[3]
print(data[index1], data[index2],data[index3], data[index4])

print(requests.post(URLsolution, data = json.dumps({"token": solve()})).text)
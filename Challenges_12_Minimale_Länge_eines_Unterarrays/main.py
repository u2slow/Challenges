import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/12/"
URLsolution = "https://cc.the-morpheus.de/solutions/12/"



def solve():
    resp = requests.get(URLchallenge).json()

    k = resp['k']
    data = resp['list']
    print("K: ", k)
    print(data)
    sol = 0
    counter = 0
    for sol in range(100000):
        for elindex in range(len(data)):
            for c in range(sol+1):
                if sol+elindex > (len(data)-1):
                    break
                counter = counter + data[c+elindex]
                #print(counter)
                if counter >= k:
                    print(sol)
                    return sol +1
            counter = 0


#print(solve())
for i in range(10):
    resp = requests.post(URLsolution, data = json.dumps({"token": solve()}))
    print(resp)
    print(resp.text)
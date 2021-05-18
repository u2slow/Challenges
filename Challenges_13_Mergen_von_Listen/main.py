import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/13/"
URLsolution = "https://cc.the-morpheus.de/solutions/13/"


def solve2(resp):
    
    a_list = resp['lista']
    b_list = resp['listb']
    sol = []
    
    x = len(a_list)+ len(b_list)
    while True:
        if len(a_list) == 0:
            sol = sol + b_list
            break
        elif len(b_list) == 0:
            sol = sol + a_list
            break
        if a_list[0] < b_list[0]:
            sol.append(a_list[0])
            del a_list[0]
        elif b_list[0] < a_list[0]:
            sol.append((b_list[0]))
            del b_list[0]
        else:
            sol.append(a_list[0])
            sol.append(b_list[0])
            del a_list[0]
            del b_list[0]
    
    return sol

#print(solve())
for i in range(5):
    resp = requests.get(URLchallenge).json()
    resp = requests.post(URLsolution, data = json.dumps({"token": solve2(requests.get(URLchallenge).json())}))
    print(resp)
    print(resp.text)
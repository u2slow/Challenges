import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/14/"
URLsolution = "https://cc.the-morpheus.de/solutions/14/"

resp = requests.get(URLchallenge).json()['list']



def compare(a_interval, b_interval):
    if a_interval[1] == b_interval[0] and a_interval[0] < b_interval[0]:
        return [a_interval[0], b_interval[1]]
    elif a_interval[0] == b_interval[1] and a_interval[1] > b_interval[1]:
        return [b_interval[0], a_interval[1]]
    elif b_interval[0] <= a_interval[0] <= b_interval[1]:
        if a_interval[1] >= b_interval[1]:
            return [b_interval[0],a_interval[1]]
        elif a_interval[1] <= b_interval[1]:
            return [b_interval[0],b_interval[1]]
    elif a_interval[0] <= b_interval[0] <= a_interval[1]:
        if a_interval[1] >= b_interval[1]:
            return [a_interval[0],a_interval[1]]
        elif a_interval[1] <= b_interval[1]:
            return [a_interval[0],b_interval[1]]
    else:
        return [0,0,0]

def solve(resp):
    i = 0
    while i < len(resp):
        n = 0
        print("h")
        while n < len(resp):
            print(n)
            if i == n:
                continue
            value = compare(resp[i], resp[n])
            del resp[i]
            del resp[n-1]
            if len(value) == 2:
                del resp[i]
                del resp[n-1]
                resp.insert(i-1, value)
            n = n + 1
        i = i + 1
    return resp
                

#print(compare([5,8],[1,5]))
print(requests.post(URLsolution, data=json.dumps({"token": solve(resp)})))
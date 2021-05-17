import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/11/"
URLsolution = "https://cc.the-morpheus.de/solutions/11/"

resp = requests.get(URLchallenge).text



def solve():
    resp = requests.get(URLchallenge).text
    counter = 0
    for i in resp:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
    if counter == 0:
        return True
    return False
        

#print(resp)
#print(solve())
for i in range(10):
    #print(resp)
    #print(solve())
    print(requests.post(URLsolution, data = json.dumps({"token": solve()})).text)
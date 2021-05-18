import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/11/"
URLsolution = "https://cc.the-morpheus.de/solutions/11/"

resp = requests.get(URLchallenge).text



def solve():
    
    
print(requests.post(URLsolution, data = json.dumps({"token": solve()})).text)
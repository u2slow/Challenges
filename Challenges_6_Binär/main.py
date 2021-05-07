import requests

URLchallenge = "https://cc.the-morpheus.de/challenges/6/"
URLsolution = "https://cc.the-morpheus.de/solutions/6/"

resp = requests.get(URLchallenge).text
print(resp)
print(bin(int(resp)))
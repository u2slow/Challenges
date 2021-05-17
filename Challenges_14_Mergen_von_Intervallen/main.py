import requests

URLchallenge = "https://cc.the-morpheus.de/challenges/14/"
URLsolution = "https://cc.the-morpheus.de/solutions/14/"

#resp = requests.get(URLchallenge).json()['list']

def solve(resp):
    pass

def compare(a_interval, b_interval):
    sol = []
    if a_interval[0] < b_interval[1] and b_interval[0] < a_interval[1]:
        sol.append(a_interval[0])
        sol.append(b_interval[1])
    elif a_interval[0] > b_interval[1] and b_interval[0] > a_interval[1]:
        sol.append(b_interval[0])
        sol.append(a_interval[1])
    
    return sol
    
print(compare([3,6], [2,5]))
import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/13/"
URLsolution = "https://cc.the-morpheus.de/solutions/13/"



def solve():
    resp = requests.get(URLchallenge).json()

    a_list = resp['lista']
    b_list = resp['listb']
    sol = []
    if len(a_list) > len(b_list):
        long_list = a_list
        short_list = b_list 
    else:
        long_list = b_list
        short_list = a_list 
    
    for i in range(len(long_list)):
        if len(short_list) == 0:
            sol = sol + long_list
            break
        if long_list[i] < short_list[0]:
            sol.append(long_list[i])
            
        elif long_list[i] > short_list[0]:
            sol.append(short_list[0])
            del short_list[0]
    
    print("a: ", a_list)
    print("b: ", b_list)
    print("sol: ", sol)

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
    
    #print("a: ", a_list)
    #print("b: ", b_list)
    #print("sol: ", sol)
    #print(x, len(sol))
    return sol

def solve3(resp):
    
    a_list = resp['lista']
    b_list = resp['listb']
    sol = a_list + b_list
    sol.sort()
    #print(sol)
    return sol

def solve4():
    resp = requests.get(URLchallenge).json()

    sol1 = solve3()
    sol2 = solve2()



#print(solve())
for i in range(5):
    resp = requests.get(URLchallenge).json()
    resp = requests.post(URLsolution, data = json.dumps({"token": solve2(requests.get(URLchallenge).json())}))
    print(resp)
    print(resp.text)
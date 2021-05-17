import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/10/"
URLsolution = "https://cc.the-morpheus.de/solutions/10/"

resp = requests.get(URLchallenge).text

#resp = "70"

print(resp)

def solve(data):
    data = data
    sol = 0.0
    i = len(data) -1
    deci_counter = 1
    counter = 0
    if data == "inf" or data == "infinity":
        return float('inf')
    while i >= 0:
        if data[i] == "0":
            pass
        elif data[i] == "1":
            sol = sol + (1*deci_counter)
        elif data[i] == "2":
            sol = sol + (2*deci_counter)
        elif data[i] == "3":
            sol = sol + (3*deci_counter)
        elif data[i] == "4":
            sol = sol + (4*deci_counter)
        elif data[i] == "5":
            sol = sol + (5*deci_counter)
        elif data[i] == "6":
            sol = sol + (6*deci_counter)
        elif data[i] == "7":
            sol = sol + (7*deci_counter)
        elif data[i] == "8":
            sol = sol + (8*deci_counter)
        elif data[i] == "9":
            sol = sol + (9*deci_counter)
        elif data[i] == "e":
            sol = 0.0
            print("data: ", data[i+1:], "realdata: ", solve(data[i+1:]))
            deci_counter = 10**(solve(data[i+1:])/10)
            print("deci: ", deci_counter)
            i = i-1
            continue
        elif data[i] == "-":
            sol = sol * -1
            i = i -1
            continue
        elif data[i] == ".":
            sol = sol * 1 / 10**counter
            deci_counter = 0.1
            print(sol)
        counter += 1
        i = i-1
        deci_counter = deci_counter * 10
    print(sol)
    return sol

#solve(resp)

print(requests.post(URLsolution, data = json.dumps({"token": solve(resp)})).text)
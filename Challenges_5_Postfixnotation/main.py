import requests
import json

URLchallenge = "https://cc.the-morpheus.de/challenges/5/"
URLsolution = "https://cc.the-morpheus.de/solutions/5/"

resp = requests.get(URLchallenge).text

data = []
start = 0
counter = 0

for i in resp:
    if i ==" ":
        data.append(resp[start:counter])
        start = counter + 1
    counter +=1
    if counter == len(resp):
        data.append(resp[counter -1])


print(data)
counter = 0
while len(data) != 1:
    if data[counter] == "+":
        value = float(data[counter -2]) + float(data[counter-1])
        symbol = "+"
    elif data[counter] == "-":
        value = float(data[counter -2]) - float(data[counter-1])
        symbol = "-"
    elif data[counter] == "*":
        value = float(data[counter -2]) * float(data[counter-1])
        symbol = "*"
    elif data[counter] == "/":
        value = float(data[counter -2]) / float(data[counter-1])
        symbol = "/"
    else:
        counter +=1
        print("no value")
        continue
    print(value)
    val1 = data[counter-1]
    val2 = data[counter-2]
    data.insert(counter - 2, value)
    data.remove(symbol)
    data.remove(val1)
    data.remove(val2)

    print(data)

    print(counter)

    counter = 0

print(requests.post(URLsolution,data=json.dumps({"token": int(data[0])})).text)

print(resp)
print(data)
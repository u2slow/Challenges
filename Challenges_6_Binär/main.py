import requests

URLchallenge = "https://cc.the-morpheus.de/challenges/6/"
URLsolution = "https://cc.the-morpheus.de/solutions/6/"

resp = requests.get(URLchallenge).text

num = "0"



def addOne(strNumber):
    for i in range(len(strNumber)):

        if strNumber[i] == "0":

            strNumber = "0"*i +"1"+ strNumber[i+1:]
            return strNumber
    
    strNumber = "0"*len(strNumber) + "1"

    return strNumber


print(bin(6))
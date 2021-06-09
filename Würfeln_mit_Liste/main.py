import random
aktiveList = []
s = input("füge neu namen hinzu, nach folgendem Muster 'Jonas;Tristan;Ben'") + ";"
start = 0
for i in range(len(s)):
    if s[i] == ";":
        name = s[start:i]
        start = i+1
        aktiveList.append(name)
i = random.random() * len(aktiveList)
print(aktiveList[int(i)])
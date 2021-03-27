import requests

feld = []

for i in range(9):
    feld.append([])
    for n in range(9):
        feld[i].append(0)

def getFeld():
    feld[0][8] = 2
    feld[1][0] = 6
    feld[1][3] = 5
    feld[1][4] = 2
    feld[1][7] = 3
    feld[2][0] = 5
    feld[2][2] = 4
    feld[2][3] = 6
    feld[3][4] = 7
    feld[4][1] = 9
    feld[4][2] = 2
    feld[4][3] = 3
    feld[4][8] = 8
    feld[5][1] = 8
    feld[5][6] = 9
    feld[5][8] = 3
    feld[6][0] = 2
    feld[6][5] = 4
    feld[6][7] = 8
    feld[7][5] = 9
    feld[7][6] = 7
    feld[7][7] = 6
    feld[8][0] = 3
    feld[8][1] = 7
    feld[8][5] = 5
getFeld()

base = "http://127.0.0.1:5000/"
respone = requests.get(base, json= {'Feld': feld})
text = respone.text
print(text)
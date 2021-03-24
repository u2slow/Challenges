import requests

feld = []

for i in range(9):
    feld.append([])
    for n in range(9):
        feld[i].append(0)

def getFeld():
    feld[0][8].value = 2
    feld[0][8].lock = True
    feld[1][0].value = 6
    feld[1][0].lock = True
    feld[1][3].value = 5
    feld[1][3].lock = True
    feld[1][4].value = 2
    feld[1][4].lock = True
    feld[1][7].value = 3
    feld[1][7].lock = True
    feld[2][0].value = 5
    feld[2][0].lock = True
    feld[2][2].value = 4
    feld[2][2].lock = True
    feld[2][3].value = 6
    feld[2][3].lock = True
    feld[3][4].value = 7
    feld[3][4].lock = True
    feld[4][1].value = 9
    feld[4][1].lock = True
    feld[4][2].value = 2
    feld[4][2].lock = True
    feld[4][3].value = 3
    feld[4][3].lock = True
    feld[4][8].value = 8
    feld[4][8].lock = True
    feld[5][1].value = 8
    feld[5][1].lock = True
    feld[5][6].value = 9
    feld[5][6].lock = True
    feld[5][8].value = 3
    feld[5][8].lock = True
    feld[6][0].value = 2
    feld[6][0].lock = True
    feld[6][5].value = 4
    feld[6][5].lock = True
    feld[6][7].value = 8
    feld[6][7].lock = True
    feld[7][5].value = 9
    feld[7][5].lock = True
    feld[7][6].value = 7
    feld[7][6].lock = True
    feld[7][7].value = 6
    feld[7][7].lock = True
    feld[8][0].value = 3
    feld[8][0].lock = True
    feld[8][1].value = 7
    feld[8][1].lock = True
    feld[8][5].value = 5
    feld[8][5].lock = True
getFeld()

base = "http://127.0.0.1:5000/"
respone = requests.get(base, json= {'Feld': feld})
text = respone.text
print(text)
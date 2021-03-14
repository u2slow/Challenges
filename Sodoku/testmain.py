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
tFeld = feld

class cell():
    def __init__(self, xposition, yposition, val):
        self.xposition = xposition
        self.yposition = yposition
        self.val = val

def findStart(iFeld):
    for i in range(9):
        for n in range(9):
            if iFeld[i][n] == 0:
                return {"x": i,
                        "y": n}

def insertParam(counter, param):
    val = cell(param["x"], param["y"], counter)
    if checkParam(val):
        tFeld[param["x"]][param["y"]] = counter
        return True
    return False

def checkParam(val):
    row = tFeld[val.xposition]
    for i in row:
        if val.val == i:
            return False
    for i in range(9):
        if val.val == tFeld[i][val.yposition]:
            return False
    return True


def checkRow(val):
    val = val
    s = sorted(tFeld[val.xposition])
    counter = 0
    for i in s:
        if s[i] != counter:
            return counter
        counter += 1

def display():
    for i in tFeld:
        print(i)
    print("")

def mainLoop():
    counter = 1
    while True:
        start = findStart(tFeld)
        display()
        print(counter)
        if insertParam(counter, start):
            counter = 1
        else:
            counter +=1
        if counter > 9:
            row = checkRow(cell (start["x"],start["y"], counter))
            counter = row

mainLoop()
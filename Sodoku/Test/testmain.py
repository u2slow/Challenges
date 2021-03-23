class point():
    def __init__(self,value,compartment):
        self.value = value
        self.lock = False
        self.compartment = compartment

listofpoints = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]],
]
feld = []

for i in range(9):
    feld.append([])
    for n in range(9):
        feld[i].append(point(0, {"x": int(i/3), "y": int(n/3)}))
        listofpoints[int(i/3)][int(n/3)].append({"x": i, "y": n})

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
tFeld = feld

def display():
    x = []
    for i in range(9):
        x.append([])
        for n in range(9):
            x[i].append(tFeld[i][n].value)
    for i in x:
        print(i)
    print("")

class cell():
    def __init__(self, xposition, yposition, val):
        self.xposition = xposition
        self.yposition = yposition
        self.val = val

def findStart(iFeld):
    for i in range(9):
        for n in range(9):
            if iFeld[i][n].value == 0:
                return {"x": i,
                        "y": n}
    return True

def insertParam(counter, param):
    val = cell(param["x"], param["y"], counter)
    if checkParam(val):
        tFeld[param["x"]][param["y"]].value = counter
        return True
    return False

def checkParam(val):
    row = tFeld[val.xposition]
    for i in row:
        if val.val == i.value:
            return False
    for i in range(9):
        if val.val == tFeld[i][val.yposition].value:
            return False
    valList = []
    for i in listofpoints[val.xposition][val.xposition]:
        valList.append(tFeld[i["x"]][i["y"]].value)
    print("v: ",valList)
    display()
    return True


def checkRow(val):
    print("check")
    val = val
    s = sorted(tFeld[val.xposition].value)
    counter = 0
    for i in s:
        if s[i] != counter:
            val.val = counter
            if checkParam(val):
                return counter
            else:
                return 10
    return 10

def findsecondStart(istart):
    start = istart
    while True:
        if start["y"] < 1:
            y = 8
            x = start["x"] - 1
        else:
            x = start["x"]
            y = start["y"] -1
        if tFeld[x][y].lock:
            start = {"x": x,
                     "y": y}
        else:
            return {"x": x,
                     "y": y}
            
def mainLoop():
    counter = 1
    start = findStart(tFeld)
    for i in range(10):
        if counter > 9:
            start = findsecondStart(start)
            if start == True:
                break
            counter = tFeld[start["x"]][start["y"]].value + 1
            tFeld[start["x"]][start["y"]].value = 0
            continue
        else:
            start = findStart(tFeld)
            if start== True:
                break
        if insertParam(counter, start):
            counter = 1
            continue
        else:
            counter += 1
            continue
    display()
    print ("fertig")

mainLoop()
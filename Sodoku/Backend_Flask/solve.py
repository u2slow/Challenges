class point():
    def __init__(self,value,compartment):
        self.value = value
        self.lock = False
        self.compartment = compartment

def getFeld(indata):
    for i in indata:
        tFeld[i[0]][i[1]].value = i[2]
        tFeld[i[0]][i[1]].lock = True
    

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
    ##Horizontal##
    row = tFeld[val.xposition]
    for i in row:
        if val.val == i.value:
            return False
    ##Vertical##
    for i in range(9):
        if val.val == tFeld[i][val.yposition].value:
            return False
    ##compartment##
    for i in listofpoints[int(val.xposition/3)][int(val.yposition/3)]:
        if tFeld[i["x"]][i["y"]].value == val.val:
            return False
    
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
            
def mainLoop(data):
    getFeld(data)
    tFeld = feld
    counter = 1
    start = findStart(tFeld)
    while True:
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
    outfeld = []
    for i in range(9):
        outfeld.append([])
        for n in tFeld[i]:
            outfeld[i].append(tFeld[i][n].value)
    return outfeld
        

if __name__ == '__main__':
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

    tFeld = feld

    mainLoop()
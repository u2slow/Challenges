
class point():
    def __init__(self,value,compartment):
        self.value = value
        self.lock = False
        self.compartment = compartment

class cell():
    def __init__(self, xposition, yposition, val):
        self.xposition = xposition
        self.yposition = yposition
        self.val = val

class clsolver():
    def __init__(self):
        self.listofpoints = [
                    [[],[],[]],
                    [[],[],[]],
                    [[],[],[]],
                    ]
        self.tfeld = []
    
    
    def display(self):
        x = []
        for i in range(9):
            x.append([])
            for n in range(9):
                x[i].append(self.tfeld[i][n].value)
        for i in x:
            print(i)
        print("")

    def displayLock(self):
        x = []
        for i in range(9):
            x.append([])
            for n in range(9):
                x[i].append(self.tfeld[i][n].lock)
        for i in x:
            print(i)
        print("")

    def findStart(self,iFeld):
        for i in range(9):
            for n in range(9):
                if iFeld[i][n].value == 0:
                    return {"x": i,
                        "y": n}
        return True

    def insertParam(self,counter, param):
        val = cell(param["x"], param["y"], counter)
        if self.checkParam(val):
            self.tfeld[param["x"]][param["y"]].value = counter
            return True
        return False

    def checkParam(self,val):
        ##Horizontal##
        row = self.tfeld[val.xposition]
        for i in row:
            if val.val == i.value:
                return False
        ##Vertical##
        for i in range(9):
            if val.val == self.tfeld[i][val.yposition].value:
                return False
        ##compartment##
        for i in self.listofpoints[int(val.xposition/3)][int(val.yposition/3)]:
            if self.tfeld[i["x"]][i["y"]].value == val.val:
                return False
        #self.display()
        return True

    def findsecondStart(self,istart):
        start = istart
        while True:
            if start["y"] < 1:
                y = 8
                x = start["x"] - 1
            else:
                x = start["x"]
                y = start["y"] -1
            if self.tfeld[x][y].lock:
                start = {"x": x,
                         "y": y}
            else:
                return {"x": x,
                         "y": y}
    def mainLoop(self):
        counter = 1
        start = self.findStart(self.tfeld)
        print("start bruteforce")
        self.display()
        while True:
            if counter > 9:
                start = self.findsecondStart(start)
                if start == True:
                    break
                counter = self.tfeld[start["x"]][start["y"]].value + 1
                self.tfeld[start["x"]][start["y"]].value = 0
                continue
            else:
                start = self.findStart(self.tfeld)
                if start== True:
                    break
            if self.insertParam(counter, start):
                counter = 1
                continue
            else:
                counter += 1
                continue
        outfeld = []
        self.display()
        for i in range(9):
            outfeld.append([])
            for n in range(9):
                outfeld[i].append(self.tfeld[i][n].value)
        self.tfeld = []
        return outfeld

    def start(self,data):
        print(data)
        for i in range(9):
            self.tfeld.append([])
            for n in range(9):
                self.tfeld[i].append(point(data[i][n],{"x": int(i/3), "y": int(n/3)}))
                self.listofpoints[int(i/3)][int(n/3)].append({"x": i, "y": n})
                if data[i][n] != 0:
                    self.tfeld[i][n].lock = True
                else:
                    self.tfeld[i][n].lock = False
        self.display()
        return self.mainLoop()
        

if __name__ == '__main__':
    solver = clsolver()
    solver.start([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        

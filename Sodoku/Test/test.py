class point():
    def __init__(self,value,compartment):
        self.value = value
        self.lock = False
        self.compartment = compartment

feld = []
for i in range(9):
    feld.append([])
    for n in range(9):
        feld[i].append(point(0, {"x": int(i/3), "y": int(n/3)}))


def display():
    x = []
    for i in range(9):
        x.append([])
        for n in range(9):
            x[i].append(feld[i][n].compartment)
    for i in x:
        print(i)
    print("")

display()
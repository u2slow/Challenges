from enum import Enum

class environment:
    def __init__(self, size, start, destination, blocketarea):
        self.blocketarea = blocketarea
        self.size = size
        self.start = start
        self.destination = destination
        self.createEnvironment()
    
    def show(self):
        plist = []
        for i in range(len(self.background)):
            plist.append([])
            for n in range(len(self.background[i])):
                plist[i].append(self.background[i][n].value)
            print(plist[i])
        print("")

    def createEnvironment(self):
        self.background = []
        for i in range(self.size):
            self.background.append([])
            for n in range(self.size):
                self.background.append(point([i,n],status.background,[]))
        for i in self.blocketarea:
            print(self.background[i[0]][i[1]].getStatus)
            self.background[i[0]][i[1]].status = status.blocked
        self.background[self.start[0]][self.start[1]] = status.start
        self.background[self.destination[0]][self.destination[1]] = status.destination
        self.search = [point(self.start, status.start)]

    def findPath(self):
        for i in self.search:
            if self.background[i.location[0]][i.location[1]] == status.destination:
                pass

class status(Enum):
    background = 0
    blocked = 1
    start = 3
    destination = 4
    search = 5
    lastsearch = 6
    searched = 7
    
class point:
    def __init__(self,location,status, parent):
        self.location = location
        self.status = status
        self.parent = parent
    def getStatus(self):
        return self.status
    def getLocation(self):
        return self.location
    def getParent(self):
        return self.parent
if __name__ == '__main__':
    env = environment(8,[1,1],[6,6], [[2,3],[3,3],[4,3]])
    env.show()

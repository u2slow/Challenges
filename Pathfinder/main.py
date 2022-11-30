from enum import Enum

class point:
    def __init__(self,location,status, parent):
        self.location = location
        self.status = status
        self.parent = parent

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
                plist[i].append(self.background[i][n].status.value)
            print(plist[i])
        print("")

    def createEnvironment(self):
        self.background = []
        for i in range(self.size):
            self.background.append([])
            for n in range(self.size):
                self.background[i].append(point([i,n],status.background,[]))
        for i in self.blocketarea:
            self.background[i[0]][i[1]].status = status.blocked
        self.background[self.start[0]][self.start[1]].status = status.start
        self.background[self.destination[0]][self.destination[1]].status = status.destination
        self.lastsearch = [self.start]

    def findPath(self):
        child = self.spread()
        print(child)
        route = [child]
        while child != self.start:
            print("n", self.background[child[0]][child[1]].location, "parent:",self.background[child[0]][child[1]].parent)
            child = self.background[child[0]][child[1]].parent
            route.append(child)
        print(route)
        for i in route:
            self.background[i[0]][i[1]].status = status.route
        self.show()
    def spread(self):
        search = set()
        while True:
            for i in self.lastsearch:
                pre_search = [(i[0]+1,i[1]),
                             (i[0]-1,i[1]),
                             (i[0],i[1]+1),
                             (i[0],i[1]-1)]
                for n in pre_search:
                    if 0 <= n[0] < self.size and 0 <= n[1] < self.size and self.background[n[0]][n[1]].status != 7:
                        if self.background[n[0]][n[1]].status.value == 4:
                            self.show()
                            return i
                        if self.background[n[0]][n[1]].status.value == 0:
                            self.background[n[0]][n[1]].status = status.searched
                            self.background[n[0]][n[1]].parent = i
                            search.add(n)
            self.show()
            self.lastsearch = list(search)

class status(Enum):
    background = 0
    blocked = 1
    start = 3
    destination = 4
    search = 5
    lastsearch = 6
    searched = 7
    route = 8

if __name__ == '__main__':
    env = environment(8,[1,1],[6,6], [[2,3],[2,1],[3,3],[4,3]])
    env.show()
    env.findPath()

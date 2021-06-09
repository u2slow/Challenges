class environment:
    def __init__(self, size, start, destination, blocketarea):
        self.blocketarea = blocketarea
        self.size = size
        self.start = start
        self.destination = destination
        self.createEnvironment()
    
    def show(self):
            for i in self.background:
                print(i)
            print("")

    def createEnvironment(self):
        self.background = []
        for i in range(self.size):
            self.background.append([])
            self.background[i] = [0]*self.size
        for i in self.blocketarea:
            self.background[i[0]][i[1]] = 1
        self.background[self.start[0]][self.start[1]] = 3
        self.background[self.destination[0]][self.destination[1]] = 4

    def findPath():
        
        

if __name__ == '__main__':
    env = environment(8,[1,1],[6,6], [[2,3],[3,3],[4,3]])
    env.show()

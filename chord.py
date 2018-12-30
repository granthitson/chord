import time, random, sys

class Chord:
    def __init__(self):
        self.B = None
        self.N = None
        self.key = None
        self.node = None
        
        self.prevNode = None
        self.nextNode = None
        
        self.nodes = []
        self.nodesBefore = []
        
        self.foundPrev = None
        self.found = None
        self.foundNext = None

    def start(self):
        self.setupB()
        self.setupN()
        self.chord()
        self.fingerTable()
        print('Console is closing in 3 minutes')
        time.sleep(180)
        sys.exit()
    

    def setupB(self):
        setupB = input("Specify B. Enter a number between 5 - 10, inclusive: ")
        try:
            self.B = int(setupB.replace(' ' ,''))
            if int(setupB) not in range(5,11):
                print("Not in range.")
                self.setupB()
            else:
                self.B = int(setupB.replace(' ' ,''))
                print("B = {}".format(self.B))
        except ValueError or TypeError:
            ("Not in range.")
            self.setupB()
            

    def setupN(self):
        setupN = input("Specify N. Enter a number between 5 - 10, inclusive: ")
        try:
            self.N = int(setupN.replace(' ' ,''))
            if int(setupN) not in range(5,11):
                ("Not in range.")
                self.setupN()
            else:
                self.N = int(setupN.replace(' ' ,''))
                print("N = {}".format(self.N))
        except ValueError or TypeError:
            ("Not in range.")
            self.setupN()
            
    def chord(self):
        print("\nSetting up Chord with {} number of nodes, ranging in value from 1-{}".format(self.N,2**self.B))
        for i in range(1,self.N+1):
            n = random.randint(1,2**self.B)
            for i in self.nodes:
                if n == i:
                    n = random.randint(1,2**self.B)
                else:
                    continue
                
            self.nodes.append(n)
        self.nodes = sorted(self.nodes)
        print(", ".join("{}: Node {}".format(num,self.node) for num,self.node in enumerate(self.nodes)))
        time.sleep(1)
        self.key = random.randint(1,2**self.B)
        self.node = self.nodes[1]
        self.prevNode = self.nodes[1]
        self.nextNode = self.nodes[2]
        print("\nStarting at NODE {}. Locating KEY {}".format(self.node,self.key))
        

    def fingerTable(self):
        reorderedList = self.nodes
        orderOfNodes = []
        if self.key < min(reorderedList):
            print("KEY {} is > than the minimum NODE {}. Defers to NODE {}.".format(self.key,min(reorderedList),reorderedList[0]))
        else:
            pass
            
        for i,v in enumerate(reorderedList):
            power = 0
            count = 1
            if self.prevNode != v:
                continue
            elif self.prevNode+2**self.B == v:
                pass
            elif i == len(reorderedList):
                self.fingerTable

            
            print("\nFingerTable for Node {}\n".format(self.prevNode))
            if self.prevNode in orderOfNodes:
                pass
            else:
                orderOfNodes.append(self.prevNode)
            
            while power < self.B:
                exp = 2**power
                k = v + exp
                if k >= max(reorderedList):
                    self.prev = max(reorderedList)
                    self.nodesBefore = reorderedList
                    reorderedList[:] = [(i + 2**self.B) for i in reorderedList]
                else:   
                    for value in reorderedList:
                        if k < value:
                            if not self.nodesBefore:
                                print("NODE {} + {} | KEY = {} | KEY Defers to NODE = {} |".format(v,exp,k,value))
                                if self.key > k and self.key < value:
                                    self.foundNext = value
                                    self.foundPrev = self.prevNode
                                    self.nextNode = self.foundNext
                                elif self.key < k and self.key > self.prevNode:
                                    self.foundNext = value
                                    self.found = value
                                    self.foundPrev = self.prevNode
                                    self.nextNode = self.foundNext
                                elif self.key > self.prevNode and self.key < k:
                                    self.foundNext = value
                                    self.foundPrev = self.prevNode
                                    self.nextNode = self.foundNext
                                elif k == self.key:
                                    self.found = value
                                    self.foundPrev = self.prevNode
                                    self.foundNext = self.nextNode
                                else:
                                    for i in reorderedList:
                                        if i > self.key:
                                            self.foundNext = i
                                            self.foundPrev = self.prevNode
                                            self.nextNode = self.foundNext
                                        else:
                                            self.prevNode = i
                                    self.nextNode = value

                            else:
                                print("NODE {} + {} | KEY = {} | KEY Defers to NODE = {} ({}) |".format(v,exp,k,value-2**self.B,value))
                                if self.key > k and self.key < value:
                                    self.prevNode = self.nextNode+2**self.B
                                    self.foundNext = value
                                    self.foundPrev = self.prevNode
                                    self.nextNode = self.foundNext
                                elif self.key < k and self.key > self.prevNode:
                                    self.foundNext = value-2**self.B
                                    self.foundPrev = self.nextNode
                                    self.foundNext = self.foundNext
                                elif self.key > self.prevNode and self.key < k:
                                    self.foundNext = value
                                    self.foundPrev = self.prevNode
                                    self.nextNode = self.foundNext
                                elif k == self.key:
                                    self.found = value-2**self.B
                                    self.foundNext = self.nextNode
                                    self.foundPrev = self.prevNode
                                else:
                                    for i in nodesBefore:
                                        if i > self.key:
                                            self.foundNext = i
                                            self.found = i
                                            self.foundPrev = self.prevNode
                                            self.nextNode = self.foundNext
                                        else:
                                            self.prevNode = i
                                    self.nextNode = value

                                    
                            power += 1
                            break
                        elif k > value:
                            self.prevNode = value
                            continue
                        
            if self.found != None and self.found == self.key:
                if not self.nodesBefore:
                    print('\nExact key value found. KEY {} found at NODE {}'.format(self.key,self.foundNext))
                else:
                    print('\nExact key value found. KEY {} found at NODE {} ({})'.format(self.key,self.found, self.foundNext+2**self.B))
                orderOfNodes.append(self.found)
                print('Visiting Order of Nodes: {}'.format(orderOfNodes))
                return
            if self.found != None and self.found != self.key:
                self.nextNode = self.foundNext
                self.prevNode = self.foundPrev
                orderOfNodes.append(self.found)
                print('Visiting Order of Nodes: {}'.format(orderOfNodes))
                continue
            elif self.found == None and self.foundNext != None and self.foundPrev != None:
                if self.foundPrev in orderOfNodes:
                    orderOfNodes.append(self.foundNext)
                elif self.foundPrev-2**self.B in orderOfNodes:
                    orderOfNodes.append(self.foundNext)
                else:
                    orderOfNodes.append(self.foundPrev)
                self.nextNode = self.foundNext
                self.prevNode = self.foundPrev
                print('Visiting Order of Nodes: {}'.format(orderOfNodes))
                continue
            elif self.found == None and self.foundNext == None and self.foundPrev == None:
                self.prevNode = self.nextNode
                orderOfNodes.append(self.prevNode)
                print('Visiting Order of Nodes: {}'.format(orderOfNodes))
            


def main():
    time.sleep(1)
    print("P2P Architecture DEMO - Chord Circular ID System with B-bits\n"
          "2^B ID spaces possible -- N number of nodes in Chord\n"
          "5 <= B <= 10 -- 5 <= N <= 10")
    time.sleep(2)
    chord = Chord()
    start = input("Type 'y' or 'n' to answer. Begin demo? ")
    if start.replace(' ','') == 'y':
        print("Beginning demo...")
        time.sleep(2)
        chord.start()
    else:
        print("Exiting..")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    main()

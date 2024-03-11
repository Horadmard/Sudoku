class Node:
    def __init__(self, value):
        self.element = value
        self.childs = []

    def getEl(self):
        return self.element

    def getNext():
        return self.nextEl

class Tree:
    def __init__(self, fnode):
        self.firstNode = fnode

    def add(self, newNode):
        self.childs.append(newNode)

    def printBFSTree(self):
        print(self.element)
        for item in self.childs:
            printBFSTree(item)
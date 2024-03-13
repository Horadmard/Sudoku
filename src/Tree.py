#Implanting Node and Tree for BackTrack algorithm

class Node:
    def __init__(self, value, pos=None):
        self.element = value
        self.pos = pos
        self.childs = []

class Tree:
    def __init__(self, fnode):
        self.firstNode = Node(fnode)

    def add(self, newNode):
        self.childs.append(newNode)

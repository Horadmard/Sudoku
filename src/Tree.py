class Node:
    def __init__(self, value):
        self.element = value
        self.pos = [-1, -1]
        self.childs = []


class Tree:
    def __init__(self, fnode):
        self.firstNode = Node(fnode)

    def add(self, newNode):
        self.childs.append(newNode)
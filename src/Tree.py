class Node:
    def __init__(self, value):
        self.element = value
        self.childs = []

    def getEl(self):
        return self.element

    def getChilds(self):
        return self.childs


class Tree:
    def __init__(self, fnode):
        self.firstNode = Node(fnode)

    def add(self, newNode):
        self.childs.append(newNode)
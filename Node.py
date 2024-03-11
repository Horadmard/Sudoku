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

    # def bfs(self):
    #     print(self.firstNode.element)
    #     queue = self.firstNode.childs
    #     visited = []

    #     for node in queue:
    #         if node not in visited:
    #             print(node.)

    # def dfs(self):
    #     pass
    
if __name__ == "__main__":
    node = Node(5)
    node2 = Node(10)

    node.childs.append(node2)
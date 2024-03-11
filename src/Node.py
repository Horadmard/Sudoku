import queue
# import networkx as nx
# import matplotlib.pyplot as plt


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

    def bfs(self):

        visited = set()
        q = queue.Queue()
        q.put(self.firstNode)
        order = []

        while not q.empty():
            node = q.get()
            if node not in visited:
                order.append(node)
                visited.add(node)
            for node in self[node]:
                if node not in visited:
                    q.put(node)
        return order

    def dfs(self, visited=None):
        if visited is None:
            visited = set()

        order = []

        if self.firstNode not in visited:
            order.append(self.firstNode)
            visited.add(self.firstNode)
        for node in self[self.firstNode]:
            if node not in visited:
                order.extend(dfs(self, visited))

        return order


if __name__ == "__main__":
    pass

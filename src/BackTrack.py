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
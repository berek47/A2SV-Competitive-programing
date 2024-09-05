class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, element):
        while self.parent[element] >= 0:
            element = self.parent[element]
        return element

    def union(self, elem1, elem2):
        root1, root2 = self.find(elem1), self.find(elem2)
        if root1 == root2:
            return
        if self.parent[root1] > self.parent[root2]:
            self.parent[root2] += self.parent[root1]
            self.parent[root1] = root2
        else:
            self.parent[root1] += self.parent[root2]
            self.parent[root2] = root1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint_set = UnionFind(len(edges))
        for connection in edges:
            vertex1, vertex2 = connection[0] - 1, connection[1] - 1
            if disjoint_set.find(vertex1) == disjoint_set.find(vertex2):
                return connection
            disjoint_set.union(vertex1, vertex2)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]

        def union(v1, v2):
            root1 = find(v1)
            root2 = find(v2)
            if root1 != root2:
                p[root1] = root2

        p = list(range(n))
        
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)

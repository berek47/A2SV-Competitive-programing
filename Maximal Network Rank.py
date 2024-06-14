class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = {i: set() for i in range(n)}
        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                connected = len(adj[i]) + len(adj[j])
                if j in adj[i]:
                    connected -= 1
                res = max(res, connected)
        return res

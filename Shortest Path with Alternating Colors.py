class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in redEdges:
            graph[u].append((v, 1))
        for u, v in blueEdges:
            graph[u].append((v, -1))

        def bfs():
            visited = []
            res = [-1] * n
            res[0] = 0
            q= deque()
            q.append([0,1])
            q.append([0,-1])
            visited.append([0,1])
            visited.append([0,-1])
            step = 0
            while q:
                step+=1
                for i in range(len(q)):
                    node, node_color = q.popleft()
                    for child,child_color  in graph[node]:
                        if child_color == -node_color:
                            if res[child]==-1:
                                res[child] = step
                            if [child,child_color] not in visited:
                                q.append([child,child_color])
                                visited.append([child,child_color])
            return res

        return bfs()

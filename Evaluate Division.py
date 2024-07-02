class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph, weights = defaultdict(list), {}
        for index, equation in enumerate(equations):
            weights[tuple(equation)] = values[index]
            weights[(equation[1], equation[0])] = 1 / values[index] 
            graph[equation[0]].append(equation[1])
            graph[equation[1]].append(equation[0])
        
        def BFS(start, destination):
            if start not in graph or destination not in graph:
                return -1
            if start == destination:
                return 1
            queue, visited = [(start, 1)], set([start])
            while queue:
                next_level = []
                for node, product in queue:
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            next_level.append((neighbor, product * weights[(node, neighbor)]))
                            if neighbor == destination:
                                return next_level[-1][-1]
                            visited.add(neighbor)
                queue = next_level.copy()
            return -1
        
        results = []
        for query in queries:
            results.append(BFS(query[0], query[1]))
        return results

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacency_list = defaultdict(set)
        in_degree = defaultdict(int)

        for parent, child in edges:
            adjacency_list[parent].add(child)
            in_degree[child] += 1
        ancestors = [set() for _ in range(n)]
        zero_in_degree_queue = deque([])
        
        for node in range(n):
            if in_degree[node] == 0:
                zero_in_degree_queue.append(node)

        while zero_in_degree_queue:
            current = zero_in_degree_queue.popleft()
            for neighbor in adjacency_list[current]:
                ancestors[neighbor] = ancestors[neighbor].union(ancestors[current])
                ancestors[neighbor].add(current)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)
        
        for i in range(len(ancestors)):
            ancestors[i] = sorted(list(ancestors[i]))
        return ancestors

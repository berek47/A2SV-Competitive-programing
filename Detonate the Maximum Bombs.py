class Solution:
    def maximumDetonation(self, bombs: List[Tuple[int, int, int]]) -> int:
        adjacency_list = defaultdict(list)
        global_visited = set()
        max_bombs = 0

        def bfs(start_index, local_visited):
            queue = deque()
            queue.append(start_index)
            local_visited.add(start_index)
            bombs_detonated = 0

            while queue:
                current = queue.popleft()
                global_visited.add(current)
                bombs_detonated += 1

                for neighbor in adjacency_list[current]:
                    if neighbor not in local_visited:
                        local_visited.add(neighbor)
                        queue.append(neighbor)
            return bombs_detonated

        for index, (x1, y1, r1) in enumerate(bombs):
            for neighbor_index, (x2, y2, r2) in enumerate(bombs):
                if neighbor_index == index:
                    continue
                if sqrt((x1 - x2)**2 + (y1 - y2)**2) <= r1:
                    adjacency_list[index].append(neighbor_index)

        for index in range(len(bombs)):
            if index not in global_visited:
                max_bombs = max(max_bombs, bfs(index, set()))
        return max_bombs

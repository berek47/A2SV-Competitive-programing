class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = {}

        while queue:
            x, y, steps = queue.popleft()
            if (x != entrance[0] or y != entrance[1]) and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                return steps
            key = (x, y)
            if key in visited:
                continue
            visited[key] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
        return -1

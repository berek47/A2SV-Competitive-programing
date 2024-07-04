class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    queue.append((row, col, 0))
        visited = set([(row, col) for row, col, _ in queue])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            current_row, current_col, current_height = queue.popleft()
            isWater[current_row][current_col] = current_height
            
            for delta_row, delta_col in directions:
                next_row, next_col = current_row + delta_row, current_col + delta_col
                if 0 <= next_row < len(isWater) and 0 <= next_col < len(isWater[0]) and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, current_height + 1))
        return isWater

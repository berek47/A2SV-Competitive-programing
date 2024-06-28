class Solution:
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    streetDirections = {
       1: [1, 3],
       2: [0, 2],
       3: [2, 3],
       4: [1, 2],
       5: [0, 3],
       6: [0, 1]
    }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int, oppositeDirection: int) -> None:

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] < 0:
                return

            v = grid[i][j]
            sd = Solution.streetDirections[v]
            direction = (oppositeDirection + 2) % 4

            if direction not in sd:
                return

            grid[i][j] = -v

            for d in sd:
                delt = Solution.directions[d]
                dfs(i+delt[0], j+delt[1], d)

        dfs(0, 0, 0)
        dfs(0, 0, 3)

        return grid[m-1][n-1] < 0

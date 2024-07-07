class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = float('-inf')
        m, n = len(grid), len(grid[0])
        for i in range(0, m - 3 + 1):
            hgsum = 0
            for j in range(0, n - 3 + 1):
                hgsum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                res = max(hgsum, res)
        return res

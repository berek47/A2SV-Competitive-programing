class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        dp = [[0]*(n) for x in range(m)]        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j - 1])
        
        return dp[m-1][n-1]

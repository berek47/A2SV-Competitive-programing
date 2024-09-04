class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        memo = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                memo[i][j] = 1
        
        for m in range(1, k + 1):
            new_memo = [[0] * n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    prob = 0
                    for move in moves:
                        new_i = i + move[0]
                        new_j = j + move[1]
                        if 0 <= new_i < n and 0 <= new_j < n:
                            prob += memo[new_i][new_j]
                    new_memo[i][j] = prob / 8
            
            memo = new_memo
        
        return memo[row][column]

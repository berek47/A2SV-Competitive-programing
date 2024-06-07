class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        
        res = []
        for i in range(col):
            res.append([0]*row)

        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]
        return res

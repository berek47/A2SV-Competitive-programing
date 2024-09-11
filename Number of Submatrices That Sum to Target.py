class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for col1 in range(n):
            for col2 in range(col1, n):
                hash = collections.defaultdict(int)
                cursum, hash[0] = 0, 1
                for row in range(m):
                    cursum += matrix[row][col2] - (matrix[row][col1 - 1] if col1 > 0 else 0)
                    res += hash[cursum - target]
                    hash[cursum] += 1
        return res

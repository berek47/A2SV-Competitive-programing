class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustount = [0] * n
        for i in trust:
            trustount[i[0] - 1] -= 1
            trustount[i[1] - 1] += 1
        for i in range(n):
            if trustount[i] == n - 1:
                return i + 1
        return -1

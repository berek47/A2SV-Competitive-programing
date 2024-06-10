class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path, k):
            if k == 0:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path, k - 1)
                path.pop()
        result = []
        backtrack(1, [], k)
        return result

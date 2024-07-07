class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        dirs = [(0, 1), (1, 0)]
        m, n = len(mat), len(mat[0])
        visited = set()
        res = []             
        queue = [(0, 0)]
        flip = True
        
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                i, j = queue.pop(0)
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                temp.append(mat[i][j])
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni >= m or nj >= n:
                        continue
                    queue.append((ni, nj))
            if flip:
                temp.reverse()
            flip = not flip
            res.extend(temp)

        return res

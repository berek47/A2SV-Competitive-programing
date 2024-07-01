class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        result = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()

        dirx = [-1, 0, 1, 0]
        diry = [0, 1, 0, -1]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append(((i, j), 0))
                    vis[i][j] = True

        while q:
            size = len(q)
            for k in range(size):
                cur = q.popleft()
                x, y = cur[0]
                count = cur[1]
                for a in range(4):
                    newx = x + dirx[a]
                    newy = y + diry[a]
                    if 0 <= newx < m and 0 <= newy < n and not vis[newx][newy]:
                        q.append(((newx, newy), count + 1))
                        vis[newx][newy] = True
                        result[newx][newy] = count + 1
        return result

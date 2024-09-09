class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x == root[x]:
                return x
            else:
                root[x] = find(root[x])
                return root[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if rank[rootY] > rank[rootX]:
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
            else:
                root[rootY] = rootX
                rank[rootX] += rank[rootY]

        stone_count = len(stones)
        max_row = max_col = 0
        for row, col in stones:
            max_row = max(max_row, row)
            max_col = max(max_col, col)

        root = [i for i in range(max_row + max_col + 2)]
        rank = [1 for i in range(max_row + max_col + 2)]
        visited = {}
        
        for row, col in stones:
            union(row, col + max_row + 1)
            visited[row] = 1
            visited[col + max_row + 1] = 1

        components = 0
        for key in visited:
            if find(key) == key:
                components += 1

        return stone_count - components

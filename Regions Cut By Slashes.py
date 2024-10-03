class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodeA, nodeB):
            rootA, rootB = find(nodeA), find(nodeB)
            if rootA != rootB:
                parent[rootA] = rootB
                nonlocal region_count
                region_count -= 1

        n = len(grid)
        region_count = n * n * 4
        parent = list(range(region_count))
        
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                cell_index = row_index * n + col_index
                if row_index < n - 1:
                    union(4 * cell_index + 2, (cell_index + n) * 4)
                if col_index < n - 1:
                    union(4 * cell_index + 1, (cell_index + 1) * 4 + 3)
                if cell == '/':
                    union(4 * cell_index, 4 * cell_index + 3)
                    union(4 * cell_index + 1, 4 * cell_index + 2)
                elif cell == '\\':
                    union(4 * cell_index, 4 * cell_index + 1)
                    union(4 * cell_index + 2, 4 * cell_index + 3)
                else:
                    union(4 * cell_index, 4 * cell_index + 1)
                    union(4 * cell_index + 1, 4 * cell_index + 2)
                    union(4 * cell_index + 2, 4 * cell_index + 3)

        return region_count

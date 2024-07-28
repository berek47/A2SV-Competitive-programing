class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        num_rows = len(grid)
        num_cols = len(grid[0])
        product_matrix = [[1 for _ in range(num_cols)] for _ in range(num_rows)]
        current_product = 1
        for i in range(num_rows):
            for j in range(num_cols):
                product_matrix[i][j] = current_product % 12345
                current_product = (current_product * grid[i][j]) % 12345
        current_product = 1
        for i in range(num_rows - 1, -1, -1):
            for j in range(num_cols - 1, -1, -1):
                product_matrix[i][j] = (product_matrix[i][j] * current_product) % 12345
                current_product = (current_product * grid[i][j]) % 12345

        return product_matrix

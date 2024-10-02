class Solution:
    def searchMatrix(self, grid: List[List[int]], value: int) -> bool:
        num_rows, num_cols = len(grid), len(grid[0])
        start, end = 0, num_rows - 1
        while start <= end:
            middle = (start + end) >> 1
            if value < grid[middle][0]:
                end = middle - 1
            elif value > grid[middle][-1]:
                start = middle + 1
            else:
                break

        row = middle
        left, right = 0, num_cols - 1
        while left <= right:
            middle = (left + right) >> 1
            if value == grid[row][middle]:
                return True
            if value < grid[row][middle]:
                right = middle - 1
            else:
                left = middle + 1

        return False

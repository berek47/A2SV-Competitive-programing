class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        previous_row = [poured]
        for i in range(1, query_row + 1):
            current_row = [0] * (i + 1)
            for j in range(i):
                overflow = previous_row[j] - 1
                if overflow > 0:
                    current_row[j] += 0.5 * overflow
                    current_row[j + 1] += 0.5 * overflow

            previous_row = current_row
        return min(1, previous_row[query_glass])

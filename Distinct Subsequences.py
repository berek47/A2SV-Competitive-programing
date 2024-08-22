class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        source_len = len(s)
        target_len = len(t)

        single_row = [0] * (target_len + 1)

        dp_table = []
        for _ in range(source_len + 1):
            dp_table.append(single_row.copy())

        for i in range(source_len + 1):
            dp_table[i][0] = 1

        for i in range(1, source_len + 1):
            for j in range(1, target_len + 1):
                dp_table[i][j] = dp_table[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp_table[i][j] += dp_table[i - 1][j - 1]

        return dp_table[source_len][target_len]

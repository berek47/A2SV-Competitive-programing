class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_hold = -math.inf
        previous_profit = 0
        for price in prices:
            temp_profit = max_profit
            max_profit = max(max_profit, max_hold + price)
            max_hold = max(max_hold, previous_profit - price)
            previous_profit = temp_profit
        return max_profit

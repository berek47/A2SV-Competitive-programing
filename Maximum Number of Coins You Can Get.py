class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        a = len(piles) // 3
        b = 0
        c = 1
        for i in range(a):
            b += piles[c]
            c += 2
        return b

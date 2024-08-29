class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=x^y
        n=str(bin(n))[2:]
        return n.count('1')

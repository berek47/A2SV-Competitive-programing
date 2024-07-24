class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prevSum = shifts[-1]
        n = len(shifts)
        res = ""
        for i in range(-2, -n-1, -1):
            shifts[i]+=prevSum
            prevSum = shifts[i]
        for i in range(n):
            res += chr(97 + (ord(s[i])%97 + shifts[i]%26)%26)
        return res

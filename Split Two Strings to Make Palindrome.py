class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.inner(a,b) or self.inner(b, a)
    
    def inner(self, a, b):
        l, r = 0, len(a) - 1
        
        ab, aa, bb = True, True, True
        while l <= r and (ab or aa or bb):
            aa = (ab or aa) and a[l] == a[r]
            bb = (ab or bb) and b[l] == b[r]
            ab = ab and a[l] == b[r]
            l, r = l+1,r-1
        return aa or ab or bb

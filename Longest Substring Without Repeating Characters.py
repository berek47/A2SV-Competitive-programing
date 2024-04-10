class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = ""
        l,r = 0,0
        ci = {}

        while r < len(s):
            c = s[r]
            if c not in ci:
                ci[c] = r  
            else:
                if ci[c]+ 1 > l:
                    l = ci[c]+1
                ci[c] = r
            
            if len(ls) < r-l+1:
                ls = s[l:r+1]

            r += 1
        
        if len(ls) < r-l:
            ls = s[l:r]   
        
        return len(ls)

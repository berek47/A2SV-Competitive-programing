class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word) < 5:
            return 0
        
        l = 0
        r = 0
        ans  = 0
        seen = set()
        
        while r < len(word):
            if word[r-1] > word[r]:
                l = r
                seen = set()

            seen.add(word[r])
            
            if len(seen) > 4:
                ans = max(ans, r - l + 1)  
                
            r += 1
        return ans

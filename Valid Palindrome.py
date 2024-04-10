class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(i for i in s if i.isalnum() )
         = a.lower()
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
        

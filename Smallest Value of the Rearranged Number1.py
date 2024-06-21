class Solution:
    def smallestNumber(self, num: int) -> int:
        digits=[]
        for i in str(num):
            if(i=='-'):
                continue
            digits.append(int(i))
        digits.sort()
        ans=""
        if(num>0):
            j = 0
            while(j<len(digits) and digits[j]==0):
                j+=1
            
            ans+=str(digits[j])
            j+=1
            ans+=('0'*digits.count(0))

            while(j<len(digits)):
                ans+=str(digits[j])
                j+=1
            
            return int(ans)  
        
        else:
            digits.sort(reverse=True)
            for i in digits:
                ans+=str(i)
            return -int(ans)
        
        

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        t = n//2
        s = sum(skill) // t 
        
        c = Counter(skill)
        lookup =Counter() 
        
        for num in skill:
            if c[num] and s- num in c and c[s-num]>0:
                c[s-num]-=1
                c[num]-=1
                lookup[(s-num, num)]+=1
        for k, v in c.items():
            if v!= 0:
                return -1
        result = 0
        for k,v in lookup.items():
            a, b = k
            result += a*b*v
            
        return result

class Solution:
    def frequencySort(self, s: str) -> str:
      
        dict= Counter(s)
 
        si=sorted(dict,reverse=True,key=lambda x:dict[x])
        Arr=[]
        for i in si:      
            Arr=Arr+[i*dict[i]]


        return "".join(Arr)

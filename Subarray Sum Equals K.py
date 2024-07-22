class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        dic={}
        for i in accumulate(nums):
            if i-k in dic:
                cnt+=dic[i-k]
            if i==k:cnt+=1
            if i in dic:dic[i]+=1
            else:dic[i]=1
        return cnt

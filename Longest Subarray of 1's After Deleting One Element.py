class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,ans,z=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:z+=1
            while z>1:
                if nums[l]==0:
                    z-=1
                l+=1
            ans=max(ans,i-l)
        return ans

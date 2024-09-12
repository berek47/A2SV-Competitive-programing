class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left,l,r,ans,n=-1,0,0,0,len(nums)
        mp={}
        while r<n:
            if nums[r] in mp:
                mp[nums[r]]+=1
            else:
                mp[nums[r]]=1
            while len(mp)>k or mp[nums[l]]>1:
                if len(mp)>k:
                    left=l
                if mp[nums[l]]>1:
                    mp[nums[l]]-=1
                else:
                    mp.pop(nums[l])
                l+=1
            if len(mp)==k:
                ans+=l-left
            r+=1
        return ans

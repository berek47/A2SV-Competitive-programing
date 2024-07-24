class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        presum=0
        for i in nums:
            if presum < 0:
                presum=0
            presum+=i
            res=max(res,presum)
        return res

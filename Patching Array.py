class Solution:
    def minPatches(self, nums, n):
        prefix_sum, res, i = 0, 0, 0
        
        while i < len(nums) and prefix_sum < n:
            if nums[i] <= prefix_sum + 1:
                prefix_sum += nums[i]
                i += 1
            else:
                prefix_sum += prefix_sum + 1
                res += 1
        
        while prefix_sum < n:
            prefix_sum += prefix_sum + 1
            res += 1
        
        return res

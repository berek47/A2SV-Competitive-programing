class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            
        if prefix_sum[0] == prefix_sum[-1]:
            return 0

        for i in range(1, len(nums)):
            if prefix_sum[-1] - prefix_sum[i] == prefix_sum[i-1]:
                return i

        return -1

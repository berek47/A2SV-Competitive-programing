class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev1 = 0
        prev2 = 0
        for num in nums:
            current = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = current
        return prev1

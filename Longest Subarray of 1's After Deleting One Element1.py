class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        rp = 1
        l = 0
        res = 0
        for r, num in enumerate(nums):
            while l < r and rp * num >= k:
                rp //= nums[l]
                l += 1
            rp *= num
            res += (r - l) + 1 if num < k else 0
        return res

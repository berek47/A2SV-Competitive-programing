class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = sum(nums[::2])
        total_odd = sum(nums[1::2])
        prefix_even = prefix_odd = 0
        count = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num
            new_even_sum = prefix_even + total_odd
            new_odd_sum = prefix_odd + total_even
            if new_even_sum == new_odd_sum:
                count += 1
            if i % 2 == 0:
                prefix_even += num
            else:
                prefix_odd += num

        return count

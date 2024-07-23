class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        previous = float('inf')
        for current in reversed(nums):
            if current > previous:
                partitions = (current + previous - 1) // previous
                previous = current // partitions
                operations += partitions - 1
            else:
                previous = current
        return operations

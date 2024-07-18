class Solution:
    def findIndices(self, nums: List[int], indexDiff: int, valueDiff: int) -> List[int]:
        minI, maxI = 0, 0

        for i in range(indexDiff, len(nums)):
            if nums[i - indexDiff] < nums[minI]: minI = i - indexDiff
            if nums[i - indexDiff] > nums[maxI]: maxI = i - indexDiff

            if nums[i] - nums[minI] >= valueDiff:
                return [minI, i]
            if nums[maxI] - nums[i] >= valueDiff:
                return [maxI, i]
        return [-1, -1]

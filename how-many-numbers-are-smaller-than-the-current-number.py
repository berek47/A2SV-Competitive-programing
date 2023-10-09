class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            count =0 
            for j in range(len(nums)):
                if nums[j] < i:
                    count += 1
            arr.append(count)
        return arr

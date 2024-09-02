class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_occurrence, twice_occurrence = 0, 0
        for num in nums:
            single_occurrence ^= num & ~twice_occurrence
            twice_occurrence ^= num & ~single_occurrence
        return single_occurrence

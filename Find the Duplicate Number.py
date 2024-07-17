class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        ptr = nums[0]
        while ptr != fast:
            ptr = nums[ptr]
            fast = nums[fast]
        return fast

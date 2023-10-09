class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        st = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j + 1 < len(nums):
                    if st[j][0] < st[j + 1][0]:
                        st[j], st[j + 1] = st[j + 1], st[j]
                    elif st[j][0] == st[j + 1][0]:
                        l = int("".join(st[j] + st[j+1]))
                        r = int("".join(st[j+1] + st[j]))
                        if l < r:
                            st[j], st[j + 1] = st[j + 1], st[j]
        return str(int("".join(st)))

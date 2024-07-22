class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftprod = [0]*n
        rightprod = [0]*n

        leftprod[0] = 1
        for i in range(1,len(nums)):
            leftprod[i] = nums[i-1]*leftprod[i-1]

        rightprod[n-1] = 1
        for i in range(n-2,-1,-1):
            rightprod[i] = nums[i+1]*rightprod[i+1]

        ans = []
        for i in range(n):
            ans.append(leftprod[i] * rightprod[i])
        
        print(ans)
        return ans

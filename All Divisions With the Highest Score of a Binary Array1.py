class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans=[len(nums)]
        maxS= nums.count(0)

        for i in range(len(nums)):
            if i==0:
                cl, cr= 0, nums.count(1)
                curS= cl+cr

            else:
                if nums[i-1]==0:
                    cl+=1
                elif nums[i-1]==1:
                    cr-=1
                curS= cl+cr
            
            if curS> maxS:
                ans.clear()
                ans.append(i)
                maxS= curS
            elif curS==maxS:
                ans.append(i)
        return ans

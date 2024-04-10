class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros=0
        nums+=[0]
        for i in range(len(nums)-1):
            if nums[i]==0:
                zeros+=1
            elif nums[i]==nums[i+1]:
                nums[i-zeros]=nums[i]*2
                nums[i+1]=0
            else:
                nums[i-zeros]=nums[i]
            
        return nums[:len(nums)-1-zeros] + [0]*zeros      

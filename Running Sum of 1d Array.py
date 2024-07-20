class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answerList = []
        sumValue = 0

        for i in range(len(nums)):
            sumValue = sumValue + nums[i]
            answerList.append(sumValue)

        return answerList

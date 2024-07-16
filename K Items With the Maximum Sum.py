class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        r=[1]*numOnes + [0]*numZeros + [-1]*numNegOnes
        Sum=0
        for i in range(k):
            Sum+=r[i]
        return Sum

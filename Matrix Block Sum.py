class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        preSum = []

        for i in range(len(mat)):
            temp = 0
            ar = []
            for j in range(len(mat[0])):
                temp += mat[i][j]
                ar.append(temp)

            preSum.append(ar)

        ans = []

        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[i])):
                lm1 = (max(0, i-k), min(i+k, len(mat)-1))
                lm2 = (max(0, j-k), min(j+k, len(mat[0])-1))
                val = 0

                for x in range(lm1[0], lm1[1]+1):
                    val += preSum[x][lm2[1]]-preSum[x][lm2[0]]+mat[x][lm2[0]]

                temp.append(val)
            ans.append(temp)

        return ans

                


        

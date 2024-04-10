class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l,r,z,ans=0,0,0,0

        while r<len(a):
            if a[r]==0:z+=1

            while z>k:
                if a[l]==0:z-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans

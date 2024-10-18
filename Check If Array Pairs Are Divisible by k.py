class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        freq = [0]*k
        for i in arr:
            freq[i % k] += 1

        for i in range(1, k//2 + 1):
            if freq[i] != freq[-i]:
                return False
        
        if k % 2 == 0:
            if freq[k//2] % 2 != 0 or freq[0] % 2 != 0:
                return False
        return True

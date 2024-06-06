class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        children = [0] * k
        ans = float('inf')
        def distribution(index):
            nonlocal ans
            if index >= n : return max(children)
            if max(children) >= ans: return ans
            for i in range(k):
                children[i] += cookies[index]
                current_unfairness = distribution(index+1)
                ans = min(ans,current_unfairness)
                children[i] -= cookies[index]
            return ans
        return distribution(0)

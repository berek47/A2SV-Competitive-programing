class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deque_ = deque()
        deque_.append((0, -1))
        curr_sum = 0
        min_len = float('inf')
        sum_to_index = {0: -1}
        
        for i in range(n):
            curr_sum += nums[i]
            while deque_ and curr_sum - deque_[0][0] >= k:
                _, j = deque_.popleft()
                min_len = min(min_len, i - j)
            if curr_sum - k in sum_to_index:
                j = sum_to_index[curr_sum - k]
                min_len = min(min_len, i - j)
            while deque_ and curr_sum <= deque_[-1][0]:
                deque_.pop()
            deque_.append((curr_sum, i))
            sum_to_index.setdefault(curr_sum, i)

        return min_len if min_len != float('inf') else -1

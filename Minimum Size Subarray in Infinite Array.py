class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        length_of_nums = len(nums)
        sum_of_nums = sum(nums)
        
        def subarray_sum_finder_helper(target):
            min_length = math.inf
            doubled_nums = nums + nums
            prefix_sums = {0: -1}
            current_sum = 0
            for i, num in enumerate(doubled_nums):
                current_sum += num
                if current_sum - target in prefix_sums:
                    min_length = min(min_length, i - prefix_sums[current_sum - target])
                prefix_sums[current_sum] = i
            return min_length if min_length < math.inf else -1

        if sum_of_nums == target:
            return length_of_nums
        elif target < sum_of_nums:
            result = subarray_sum_finder_helper(target)
            return result
        else:
            updated_target = target % sum_of_nums
            full_cycles = target // sum_of_nums
            if updated_target == 0: return full_cycles * length_of_nums
            result = subarray_sum_finder_helper(updated_target)
            return (result + full_cycles * length_of_nums) if result != -1 else -1

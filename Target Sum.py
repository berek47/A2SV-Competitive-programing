class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums or sum(nums) < target:
            return 0

        sum_ways = {0: 1}
        for idx in range(len(nums)):
            next_sum_ways = {}
            for current_sum in sum_ways:
                pos_sum = current_sum + nums[idx]
                neg_sum = current_sum - nums[idx]

                if pos_sum in next_sum_ways:
                    next_sum_ways[pos_sum] += sum_ways[current_sum]
                else:
                    next_sum_ways[pos_sum] = sum_ways[current_sum]

                if neg_sum in next_sum_ways:
                    next_sum_ways[neg_sum] += sum_ways[current_sum]
                else:
                    next_sum_ways[neg_sum] = sum_ways[current_sum]

            sum_ways = next_sum_ways
        
        return sum_ways[target] if target in sum_ways else 0

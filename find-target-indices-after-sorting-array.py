class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        if target not in d:
            return []
        start = sum([v for k, v in d.items() if k < target])
        end = start + d[target]
        return list(range(start, end))

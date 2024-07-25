class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans = float('inf')
        total_quality = 0
        max_heap = []

        for q, w in sorted(zip(quality, wage), key=lambda x: x[1] / x[0]):
            total_quality += q
            heapq.heappush(max_heap, -q)
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            if len(max_heap) == k:
                ans = min(ans, total_quality * (w / q))

        return ans

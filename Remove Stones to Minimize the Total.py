class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pilesHeap = []
        for item in piles:
            heapq.heappush(pilesHeap, -item)
        while k > 0:
            heapq.heappush(pilesHeap, floor(heapq.heappop(pilesHeap) / 2))
            k -= 1
        return sum([-1 * i for i in pilesHeap])

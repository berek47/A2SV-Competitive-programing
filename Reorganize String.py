class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for char, count in counter.items():
            if count > ceil(len(s) / 2): return ""
            heapq.heappush(heap, ((-1) * count, char))
        last = None
        res = ""
        while heap or last:
            (count, char) = heapq.heappop(heap)
            res += char
            count += 1
            if last:
                heapq.heappush(heap, last)
            last = (count, char) if count < 0 else None
        return res

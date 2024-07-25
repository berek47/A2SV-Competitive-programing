class SmallestInfiniteSet:

    def __init__(self):
        self.current_num = 1
        self.min_heap = []
        self.s = set()

        heapq.heapify(self.min_heap)
        

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest_num = heapq.heappop(self.min_heap)
            self.s.remove(smallest_num)
            return smallest_num
        
        else:
            smallest_num = self.current_num
            self.current_num += 1
            return smallest_num
        

    def addBack(self, num: int) -> None:
        if num < self.current_num and num not in self.s:
            self.s.add(num)
            heapq.heappush(self.min_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

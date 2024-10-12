class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        temp = [0] * n
        empty = []
        used = []
        meetings = sorted(meetings, key=lambda x: x[0])
        i = 0
        for i in range(n):
            empty.append(i)
        heapify(used)
        i = st = 0
        while i < len(meetings):
            l, r = meetings[i][0], meetings[i][1]
            if l > st:st = l
            dur = r - l
            while used and used[0][0] <= st:
                room = heappop(used)[1]
                heappush(empty, room)
            if not empty:
                st = used[0][0]
                while used and used[0][0] <= st:
                    room = heappop(used)[1]
                    heappush(empty, room)
            avl = heappop(empty)
            temp[avl] += 1
            heappush(used, (st + dur,avl))
            i += 1
        mx = -math.inf 
        room = None
        for i, j in enumerate(temp):
            if j > mx:
                mx = j
                room = i
        return room

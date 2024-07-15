class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_list = [(start, duration, index) for index, (start, duration) in enumerate(tasks)]
        
        task_list.sort(key=lambda x: x[0])
        min_heap = []
        result = []
        current_time = task_list[0][0]
        
        while task_list or min_heap:
            while task_list and task_list[0][0] <= current_time:
                start_time, processing_time, task_index = task_list.pop(0)
                heapq.heappush(min_heap, (processing_time, task_index))
            
            if min_heap:
                duration, index = heapq.heappop(min_heap)
                current_time += duration
                result.append(index)
            else:
                current_time = task_list[0][0]
        
        return result

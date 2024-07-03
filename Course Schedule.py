class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = [[] for _ in range(numCourses)] 
        
        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
        
        visited = [0] * numCourses
        in_degree = [0] * numCourses
        course_order = []
        queue = deque()
       
        for course in range(numCourses):
            for neighbor in course_graph[course]:
                in_degree[neighbor] += 1

        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            current_course = queue.popleft()
            course_order.append(current_course)
            
            for neighbor in course_graph[current_course]:
                if in_degree[neighbor] != 0:
                    in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(course_order) != numCourses:
            return False
        return True

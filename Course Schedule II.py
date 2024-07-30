class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course, status):
            if status[course] == -1:
                return False
            if status[course] == 1:
                return True
            status[course] = -1
            for next_course in graph[course]:
                if not dfs(next_course, status):
                    return False
            order.append(course)
            status[course] = 1
            return True

        graph = [[] for _ in range(numCourses)]
        order = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        status = [0] * numCourses
        for course in range(numCourses):
            if not dfs(course, status):
                return []
        return order[::-1]

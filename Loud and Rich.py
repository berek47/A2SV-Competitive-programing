class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        indegree = [0] * n
        min_quiet = deepcopy(quiet)
        result = [i for i in range(n)]
        graph = [[] for _ in range(n)]
        queue = deque()
        
        for richer_person, poorer_person in richer:
            graph[richer_person].append(poorer_person)
            indegree[poorer_person] += 1
        
        for person in range(n):
            if indegree[person] == 0:
                queue.append(person)
        
        while queue:
            person = queue.popleft()
            for next_person in graph[person]:
                indegree[next_person] -= 1
                if min_quiet[next_person] > min_quiet[person]:
                    min_quiet[next_person] = min_quiet[person]
                    result[next_person] = result[person]
                if indegree[next_person] == 0:
                    queue.append(next_person)
        
        return result

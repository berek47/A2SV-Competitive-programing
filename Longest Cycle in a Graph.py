class Solution:
    def longestCycle(self, graph: List[int]) -> int:
        n = len(graph)
        longest = -1
        visited = [False] * n 
        memo = [0] * n 
        
        for start in range(n):
            if not visited[start]:
                slow = start
                fast = start
                
                while graph[fast] != -1 and graph[graph[fast]] != -1:
                    slow = graph[slow]
                    fast = graph[graph[fast]]
                    
                    if slow == fast:
                        cycleLen = 1
                        slow = graph[slow]
                        
                        while slow != fast: 
                            cycleLen += 1
                            slow = graph[slow]
                            
                        longest = max(longest, cycleLen) 
                        memo[start] = cycleLen
                        visited[start] = True 
                        break
                    
                    if memo[slow] != 0:
                        memo[start] = memo[slow]
                        visited[start] = True
                        break
        
        return longest

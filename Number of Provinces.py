class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(connections, visited, current_city):
            visited[current_city] = True
            for neighbor in range(num_cities):
                if not visited[neighbor] and connections[current_city][neighbor] == 1:
                    dfs(connections, visited, neighbor)

        num_cities = len(isConnected)
        visited = [False] * num_cities
        province_count = 0

        for city in range(num_cities):
            if not visited[city]:
                province_count += 1
                dfs(isConnected, visited, city)

        return province_count

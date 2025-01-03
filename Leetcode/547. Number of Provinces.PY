from collections import deque
class Solution:
    def findCircleNum(self,grid):
        m  = len(grid)
        n = len(grid[0])
        
        v = len(grid)
        visited = set()
     
        adj_list = {}
        # Now make a adjacency list
        for i in range(m):
            adj_list[i] = []
            for j in range(n):
                if grid[i][j] == 1 and i !=j:
                   adj_list[i].append(j)
                
        def bfs(node):
            visited.add(node)
            queue = deque()
            queue.append(node)
            while(queue):
                node = queue.popleft()
                for neighbhor in adj_list[node]:
                    if neighbhor not in visited:
                        visited.add(neighbhor)
                        queue.append(neighbhor)
        
        # def dfs(node):
        #     visited.add(node)
            
        #     for neighbhor in adj_list[node]:
        #         if neighbhor not in visited:
        #             dfs(neighbhor)
        #     return visited
                
        cnt = 0
        for vertex in range(v):
            if vertex not in visited:
                cnt += 1
                bfs(vertex)
               
        return cnt
        
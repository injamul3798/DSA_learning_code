from collections import deque
class Solution:
    def updateMatrix(self,grid):
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        visited = set()
        
        distance = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(None)
            distance.append(row)
            
        # Now lets insert those element which value is 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue.append(((i,j),0))
                    visited.add((i,j))
                    
        while queue:
            cell,steps = queue.popleft()
            nr,nc = cell
            distance[nr][nc] = steps
            
            for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
                newr = nr + i
                newc = nc + j
                
                if (newr>=0 and newr<m) and (newc>=0 and newc<n) and (grid[newr][newc]==1) and (newr,newc) not in  visited:
                    queue.append(((newr,newc),steps+1))
                    visited.add((newr,newc))
                
        return distance
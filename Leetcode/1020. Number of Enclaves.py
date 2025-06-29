from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        queue = deque()

        m = len(grid)
        n = len(grid[0])
        # first find out the boundary region 1 
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                
        while queue:
            r,c = queue.popleft()
            for mm,nn in [(0,-1),(0,1),(-1,0),(1,0)]:
                newr = r + mm
                newc = c + nn
                if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] == 1 and (newr, newc) not in visited:
                    queue.append((newr,newc))
                    visited.add((newr,newc))

        cnt  = 0
        for p in range(m):
            for q in range(n):
                if grid[p][q]==1 and (p,q) not in visited:
                    cnt += 1
        return cnt

       

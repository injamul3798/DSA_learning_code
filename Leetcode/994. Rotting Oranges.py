from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        time = 0
        while queue:
            for _ in range(len(queue)):
                nr,nc =queue.popleft()
                
                for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r = nr + i
                    c = nc + j
                    if (r>=0 and r<m) and (c>=0 and c<n) and (grid[r][c] == 1):
                        grid[r][c]=2
                        queue.append((r,c))
                        fresh_count -= 1
            if queue:
                time += 1

        if fresh_count == 0:
            return time
        return -1

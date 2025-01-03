from collections import deque
class Solution:
    def numIslands(self, grid):
        
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def bfs(row,col,grid,visited):
            # first mark that ceel visited
            visited.add((row,col))
            
            m = len(grid)
            n = len(grid[0])
            # then append the cell to queue
            queue = deque()
            queue.append((row,col))
            
            while(queue):
                r,c = queue.popleft()
                
                for i in range(-1,2):
                    for j in range(-1,2):
                        nr = r + i
                        nc = c + j
                        
                        if 4(nr>=0 and nr < m) and (nc>=0 and nc <n) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                            bfs(nr,nc,grid,visited)
                            queue.append((nr,nc))
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    cnt += 1
                    bfs(i,j,grid,visited)
                    
        print(cnt)

if __name__ == '__main__':
    grid = [
        ['1', '1', '0', '0', '0'],
        ['0', '1', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '0', '0', '0', '0'],
        ['1', '0', '1', '1', '0']
    ]
    ob = Solution()
    ob.numIslands(grid)

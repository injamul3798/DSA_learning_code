from collections import deque
class Solution:
    def numIslands(self, grid):
        
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(row,col,grid,visited):
            visited.add((row,col))
            m = len(grid)
            n = len(grid[0])
            # if we want to avoid using diagonal cell
            # then loop will be like this
            #for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:

            for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            
            
                    nr = row + i
                    nc = col + j
                    if (nr>=0  and nr<m) and (nc>=0 and nc <n) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        dfs(nr,nc,grid,visited)
                        
                    
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    cnt += 1
                    dfs(i,j,grid,visited)
                    
        print('No of island: ',cnt)

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

#User function Template for python3

class Solution:
    def numProvinces(self, grid, v):
        # code here 
        m = len(grid)
        n = len(grid[0])
        ans = {}
        for i in range(m):
            ans[i] = []
            for j in range(n):
                if grid[i][j] == 1:
                    ans[i].append(j)
        def dfs(node,visited):
            if node not in visited:
                visited.add(node)
            for neighbhor in ans[node]:
                if neighbhor not in visited:
                    dfs(neighbhor,visited)
        cnt = 0
        visited = set()
        for node in range(v):
            if node not in visited:
                dfs(node,visited)
                cnt += 1
        return cnt
        
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        v = int(input())
        grid = []
        for i in range(v):
            lis = list(map(int,input().split()))
            grid.append(lis)
        obj = Solution()
        print(obj.numProvinces(grid,v))

        
from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        ans = image
        m  = len(image)
        n = len(image[0])
                
        
        # get the inital color
        initial = False
        for i in range(m):
            for j in range(n):
                if i == sr and j == sc:
                    inital_color = image[i][j]
                    initial = True
                    break
            if initial:
                break
        visited = set()
        # def bfs(sr,sc,image):
        #     visited.add((sr,sc))
        #     ans[sr][sc] = newColor
            
        #     queue = deque()
            
        #     queue.append((sr,sc))
            
        #     while(queue):
        #         nr,nc = queue.popleft()
                
        #         m = len(image)
        #         n = len(image[0])
                
        #         for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
        #             newr = nr + i
        #             newc = nc + j
                    
        #             if (newr>= 0 and newr <m ) and (newc>=0 and newc<n) and image[newr][newc] == inital_color and (newr,newc) not in visited:
        #                  visited.add((newr,newc))
        #                  ans[newr][newc] = newColor
        #                  queue.append((newr,newc))       
        #     return ans
     
        # return bfs(sr,sc,image)
        def dfs(sr,sc,image):
            visited.add((sr,sc))
            ans[sr][sc] = newColor
            
            for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
                    newr = sr + i
                    newc = sc + j
                    
                    if (newr>= 0 and newr <m ) and (newc>=0 and newc<n) and image[newr][newc] == inital_color and (newr,newc) not in visited:
                         dfs(newr,newc,image)
            return ans
            
        return dfs(sr,sc,image)

if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    ob  = Solution()
    ob.floodFill(image,sr,sc,newColor)
        
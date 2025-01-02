class Solution:
    visited = set() 
    def numProvinces(self,adj,v):
        adj_list = {}
        # for i in range(v):
        #     adj_list[i] = []
        for i in range(v):
            adj_list[i] = []
            for j in range(v):
                if adj[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        visited = set()
        cnt = 0
        def dfs(node):
            visited.add(node)
            
            for neighbhor in adj_list[node]:
                if neighbhor not in visited:
                    dfs(neighbhor)
            return visited
            
        for i in range(v):
            if i not in visited:
                cnt += 1
                dfs(i)

        print('Total no of provinces: ',cnt)
              
    # def dfs(self,node):
    #     self.visited.add(node)
        
    #     for neighbhor in 
        
#         0 1 2 
        
        
# [1, 0, 1],
#  [0, 1, 0],
#  [1, 0, 1]
        
            
             

        print(adj_list)
        

if __name__ == '__main__':
    v = int(input())
    adj = []
    for i in range(v):
       row = list(map(int,input().split()))
       adj.append(row)
   
    ob = Solution()
    ob.numProvinces(adj,v)
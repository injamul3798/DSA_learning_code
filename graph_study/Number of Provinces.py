#User function Template for python3

class Solution:
    
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

        return cnt
              

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
        print("~")
# } Driver Code Ends
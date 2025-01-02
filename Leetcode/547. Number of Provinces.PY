class Solution(object):
    def findCircleNum(self, adj):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        v = len(adj)
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

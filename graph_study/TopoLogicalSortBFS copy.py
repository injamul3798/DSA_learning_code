from collections import deque


# Find the indegree of every Vertex
# If any vertex indegree is zero then
# pushed it into queue and reduce
# its adjacence list elements incoming degree
def TopoLogicalSortBFS(graph):
    indegree = {}
    
    # First intialize every vertex index to 0
    for u in graph:
        indegree[u] = 0
     
    # Find the incoming degree for every vertex   
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    # Store zero incoming degree vertex
    queue = deque()
    for u in indegree:
        if indegree[u] == 0:
            queue.append(u)
    
    
    topolist = []
    while queue:
        current = queue.popleft()
        topolist.append(current)
        
        for v in graph[current]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
                
    if len(topolist) == len(indegree):
        return topolist
    else:
        raise Exception("Graph has at least one cycle")

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print(TopoLogicalSortBFS(graph))

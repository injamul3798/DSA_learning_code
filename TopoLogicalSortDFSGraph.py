# Enter your code here. Read input from STDIN. Print output to STDOUT
def TopoLogicalSortDFS(graph):
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        # visit neighbor of present vertext,
        # if there is no  neighbor of this present
        # Vertext then it will return null
        for neighbor in graph.get(vertex,[]):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)
                
    # Visit every vertex of graph        
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    return stack[::-1]
    
"""

1. The get method is used to retrieve the value (neighbors) 
associated with the key vertex in the dictionary graph.
2. If vertex does not exist in the graph dictionary, 
the get method returns the default value [] (an empty list).
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
graph.get('A')       # Returns ['B', 'C']
graph.get('C')       # Returns [] (C has no neighbors)
graph.get('E', [])   # Returns [] (E is not in the graph)
"""
            
    
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}
order = TopoLogicalSortDFS(graph)
print(order)

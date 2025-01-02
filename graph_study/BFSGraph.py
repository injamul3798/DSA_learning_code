from collections import deque
def BFSGraph(graph,start):
    visited = set()
    visited.add(start)
    element = deque([start])
    while(element):
        currentNode = element.popleft()
        for node in graph[currentNode]:
            if node not in visited:
                visited.add(node)
                element.append(node)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
# Start DFS from node 'A'
visited_nodes = BFSGraph(graph, 'A')
print(visited_nodes)

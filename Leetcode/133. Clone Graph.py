"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone

            for neighbhor in node.neighbors:
                # if neighbhor not in visited:
                    clone.neighbors.append(dfs(neighbhor))
            return clone
        return dfs(node)

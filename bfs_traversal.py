from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bfs_traversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        result = []  # This will store the nodes level by level
        queueElement = deque()  # Queue to manage nodes at each level
        queueElement.append(root)

        while queueElement:
            current_at_level = len(queueElement)  # Number of nodes at the current level
            current_level = []  # List to hold nodes at the current level

            for _ in range(current_at_level):
                current = queueElement.popleft()  # Dequeue the current node
                current_level.append(current.val)  # Add the node's value to the current level

                # Enqueue the child nodes of the current node
                if current.left:
                    queueElement.append(current.left)
                if current.right:
                    queueElement.append(current.right)

            result.append(current_level)  # Add the current level to the result

        return result

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

solution = Solution()
print(solution.bfs_traversal(root))  # Output: [[1], [2, 3], [4, 5, 6]]

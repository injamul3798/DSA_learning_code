# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        element = deque()
        element.append(root)
        result = []
        while element:
            currentAtLevel = len(element)
            temp = []
            while(currentAtLevel):
                current = element.popleft()
                temp.append(current.val)
                if current.left:
                    element.append(current.left)
                if current.right:
                    element.append(current.right)

                currentAtLevel -= 1

            result.append(temp)

        return result

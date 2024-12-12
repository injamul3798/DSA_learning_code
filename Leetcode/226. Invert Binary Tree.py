# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        elm = deque([root])
        ans = root
        while(elm):
            currentLevel = len(elm)
            while(currentLevel):
                current = elm.popleft()
                current.left,current.right = current.right,current.left
                if current.left:
                   elm.append(current.left)
                if current.right:
                   elm.append(current.right)
                currentLevel -= 1
        return root

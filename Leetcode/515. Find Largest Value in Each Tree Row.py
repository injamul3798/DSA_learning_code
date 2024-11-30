# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        element = deque([root])
        ans = []
         
       
        while(element):
            currentLevelElement = len(element)
            mx = float('-inf')
            while(currentLevelElement):
                node = element.popleft()
                mx = max(mx,node.val)
                if node.left:
                    element.append(node.left)
                    
                if node.right:
                    element.append(node.right)
                currentLevelElement -= 1
            ans.append(mx)
        return ans

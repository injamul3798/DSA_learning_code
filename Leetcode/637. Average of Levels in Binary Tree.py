# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        element = deque([root])
        avg = []
        while(element):
            level_elm = len(element)
            level = level_elm
            sm = 0.0
            while(level_elm):
                current = element.popleft()
                sm += current.val
                if current.left:
                    element.append(current.left)
                if current.right:
                    element.append(current.right)
                
                level_elm -= 1
            # temp = float(sm/level)
            avg.append(sm/level)
        return avg
        

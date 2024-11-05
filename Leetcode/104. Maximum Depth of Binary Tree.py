# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        elementQueue  = deque()
        elementQueue.append(root)
        numOfLevels = -1

        while True:
            nodeCountAtLevel = len(elementQueue)
            if nodeCountAtLevel == 0:
                return numOfLevels+1
            
            while(nodeCountAtLevel >0):
                element = elementQueue.popleft()

                if element.left:
                    elementQueue.append(element.left)
                if element.right:
                    elementQueue.append(element.right)
                
                nodeCountAtLevel -= 1

            numOfLevels += 1

        return numOfLevels+1
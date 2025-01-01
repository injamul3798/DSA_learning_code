# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        queue = deque([root])
        ans = []
        # ans.append(root.val)
        while(queue):
            level_elem = len(queue)
            # while(level_elem):
            #     current = queue.popleft()
            #     if current.left:
            #         queue.append(current.left)
            #     if current.right:
            #         queue.append(current.right)
            #         ans.append(current.right.val)
                
            #     level_elem -= 1

            # elemnt = 2  ( 2,3) = 0,1

            for i in range(level_elem):
                current = queue.popleft()
                if i ==  level_elem - 1:
                    ans.append(current.val)
                 
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right) 
        #ans.sort()
        return ans
        
        

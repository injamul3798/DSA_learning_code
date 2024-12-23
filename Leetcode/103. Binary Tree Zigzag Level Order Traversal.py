# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        element = deque([root])
        res = []
        cnt = 0
        while(element):
            levelElm = len(element)
            temp = []
            cnt += 1
            while(levelElm):
                current = element.popleft()
                temp.append(current.val)
                if current.left:
                    element.append(current.left)
                if current.right:
                    element.append(current.right)
                levelElm -= 1
            if cnt%2==1:
               res.append(temp)
            else:
                # res.append(temp.sort(reverse = True))
                res.append(temp[::-1])
            #cnt += 1
        return res


            
        

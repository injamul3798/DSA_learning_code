# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        def level_order_with_adjustments(root):
            if not root:
                return []

            element = deque()
            element.append(root)
            result = []

            while element:
                currentAtLevel = len(element)
                temp = []
                for _ in range(currentAtLevel):
                    current = element.popleft()
                    if current:
                        temp.append(current.val)
                        element.append(current.left)
                        element.append(current.right)
                    else:
                        temp.append(None)

                result.append(temp)

            return result

        p_result = level_order_with_adjustments(p)
        q_result = level_order_with_adjustments(q)

        return p_result == q_result

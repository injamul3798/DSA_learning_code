# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        elm = deque([root])
        ans = set()
        while(elm):
             
            current = elm.popleft()
            ans.add(current)
            current.left,current.right = current.right,current.left
            if current.left:
                elm.append(current.left)
            if current.right:
                elm.append(current.right)
            
                
        return len(ans)
        

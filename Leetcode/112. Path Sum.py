# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        def DFSRecursive(root,path):
            if root is None:
                return False
            path.append(root.val)
            if root.left is None and root.right is None and targetSum==sum(path):
                return True
            else:
                left_checker = DFSRecursive(root.left,path)
                right_checker = DFSRecursive(root.right,path)
             
            path.pop()
            return left_checker or right_checker

        path = []
        ans = DFSRecursive(root,path)
        return ans if ans else False
        

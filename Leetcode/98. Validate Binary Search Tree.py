# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res = []
        self.inorderTraversal(root,res)
        for i in range(1,len(res)):
            if res[i-1] >= res[i]:
                return False
        return True

    def inorderTraversal(self,root,res):
        if root is None:
            return
        self.inorderTraversal(root.left,res)
        res.append(root.val)
        self.inorderTraversal(root.right,res)
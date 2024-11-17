# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def PreOrderTraversal(root,res):
            if root is None:
                return 
            res.append(root.val)
            if root.left:
                PreOrderTraversal(root.left,res)
            if root.right:
                PreOrderTraversal(root.right,res)
        res = []
        PreOrderTraversal(root,res)
        res.sort()
        cnt = 0
        ans = 0
        for i in range(k):
            ans = res[i]
        return ans

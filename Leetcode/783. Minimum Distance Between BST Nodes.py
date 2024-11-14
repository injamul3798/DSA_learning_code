# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        def dfsRecursive(root, res):
            if root is None:
                return
            res.append(root.val)
            if root.left:
                dfsRecursive(root.left, res)
            if root.right:
                dfsRecursive(root.right, res)

        res = []
        dfsRecursive(root, res)
        res.sort() 

        minDiff = float('inf')
        for i in range(1,len(res)):
            minDiff = min(minDiff,res[i]-res[i-1])
        return minDiff

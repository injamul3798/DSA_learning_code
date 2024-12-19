# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        res = []
        def dfs(root,path,csum):
            if root is None:
                return
            path.append(root.val)
            csum += root.val
            if root.left is None and root.right is None:
                if csum == targetSum:
                    res.append(list(path))
                     

            dfs(root.left,path,csum)
            dfs(root.right,path,csum)
            path.pop()
        path = []
        csum= 0
        dfs(root,path,csum)
        return res
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root is None:
            return 
        def DFSTraversalRecursive(root,path,ans):
            if root is None:
                return
            path.append(str(root.val))
            if root.left is None and root.right is None:
                ans.append("->".join(path))
            else:
                DFSTraversalRecursive(root.left,path,ans)
                DFSTraversalRecursive(root.right,path,ans)
            path.pop()

        ans = []
        path = []
        DFSTraversalRecursive(root,path,ans)
        return ans
        

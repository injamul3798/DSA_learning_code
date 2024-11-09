# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        self.findInorderList(root,ans)
        return ans

    def findInorderList(self,root,ans):
        if root is None:
            return 
        self.findInorderList(root.left,ans)
        ans.append(root.val)
        self.findInorderList(root.right,ans)

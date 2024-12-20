# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        csum = 0
        def dfs(root,path):
            if root is None:
                return
            path.append(root.val)
            # csum += root.val
            if root.left is None and root.right is None:
                # if csum == targetSum:
                #     res.append(list(path))
                s = ""
                for elm in path:
                    s += str(elm)
                res.append(int(s))

            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()

        path = []
        # csum= 0
        dfs(root,path)
        totalsum = sum(res)
        return totalsum
        # return res
        

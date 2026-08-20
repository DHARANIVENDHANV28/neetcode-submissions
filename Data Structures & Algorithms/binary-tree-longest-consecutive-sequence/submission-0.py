# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node,length):
            nonlocal res
            if not node:
                return None
            res = max(res,length)
            if node.left:
                if node.val+1 == node.left.val:
                    dfs(node.left,length+1)
                else:
                    dfs(node.left,length)
            if node.right:
                if node.val+1 == node.right.val:
                    dfs(node.right,length+1)
                else:
                    dfs(node.right,length)                   
            return None
        dfs(root,1)
        return res

        
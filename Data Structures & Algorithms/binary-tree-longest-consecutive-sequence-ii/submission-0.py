# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return (0,0)

            linc,ldec = dfs(node.left)
            rinc, rdec = dfs(node.right)

            inc = 1
            dec = 1

            if node.left:
                if node.left.val+1 == node.val: #inc
                    inc = max(inc,linc+1)
                if node.left.val-1 == node.val:
                    dec = max(dec,ldec+1)
            
            if node.right:
                if node.right.val+1 == node.val:
                    inc = max(inc,rinc+1)
                if node.right.val-1 == node.val:
                    dec = max(dec,rdec+1)
            
            res = max(res,inc+dec-1)

            return (inc,dec)
                            
        dfs(root)
        return res
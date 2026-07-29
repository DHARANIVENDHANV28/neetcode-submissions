# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.max_node = 0
        def dfs(node,val):
            if not node:
                return
            if node.val >= val:
                print(node.val,val)
                val = node.val
                self.max_node += 1 
            dfs(node.left,val)
            dfs(node.right,val)
        dfs(root,root.val)
        return self.max_node
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        def dfs(node):
            if not node:
                return -1
                
            left = dfs(node.left)
            right = dfs(node.right)
            height = 1+max(left,right)

            if height == len(res):
                res.append([])
            res[height].append(node.val)
            return height
        
        dfs(root)
        return res

        
        # def dfs(node):
        #     nonlocal leaves
        #     if not node:
        #         return None
        #     if not node.right and not node.left:
        #         leaves.append(node.val)
        #         return None
        #     node.left = dfs(node.left)
        #     node.right = dfs(node.right)
        #     return node
        
        # res = []
        # while root:
        #     leaves = []
        #     root = dfs(root)
        #     res.append(leaves)
        # return res




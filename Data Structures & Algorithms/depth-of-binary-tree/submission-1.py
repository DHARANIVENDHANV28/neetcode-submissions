# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depth = 0
    d = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = []
        def dfs(node,d):
            if not node:
                depth.append(d)
                return
            else:
                d+=1
                dfs(node.left,d)
                dfs(node.right,d)
                d-=1
        dfs(root,0)
        return max(depth)
        

        # if not root:
        #     depth = max(d,depth)
        #     return 
        # else:
        #     d += 1
        #     self.maxDepth(root.left)
        #     delf.maxDepth(root.right)
        #     d -= 1
        # return depth
        
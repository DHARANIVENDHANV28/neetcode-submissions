# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        #post order traversal
        res = 0
        def dfs(node): #return Sum, num of nodes
            nonlocal res
            if not node:
                return 0,0
                
            leftSUM,leftNode = dfs(node.left)
            rightSUM,rightNode = dfs(node.right)

            TotalSUM = leftSUM + rightSUM + node.val
            TotalNodes = leftNode + rightNode + 1
            res = max(res,TotalSUM/TotalNodes)
        
            return TotalSUM, TotalNodes
        
        dfs(root)
        
        return res
        

        
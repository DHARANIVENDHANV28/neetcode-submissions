# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        HashMap = {} #{(row,col):node.val}
        c_min,c_max = float('+inf'), float('-inf')
        r_max = 0 
        
        def dfs(node,row,col):
            nonlocal c_min,c_max,r_max
            
            if not node:
                return None

            if (row,col) not in HashMap:
                HashMap[(row,col)] = []
            HashMap[(row,col)] += [node.val]
            
            c_min = min(c_min,col)
            c_max = max(c_max,col)
            r_max = max(r_max,row)
            
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
            return None
        dfs(root,0,0)

        res = []

        for c in range(c_min,c_max+1):
            col = []
            for r in range(0,r_max+1):
                if (r,c) in HashMap:
                    col.extend(HashMap[(r,c)])
            res.append(col)

        return res
        
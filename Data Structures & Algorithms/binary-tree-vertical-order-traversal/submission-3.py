# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        HashMap = {} #{(row,col):node.val}

        if not root:
            return []

        def dfs(node,row,col):
            if not node:
                return None
            # if col not in HashMap:
            #     HashMap[col] = []
            if (row,col) not in HashMap:
                HashMap[(row,col)] = []
            HashMap[(row,col)] += [node.val]
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
            return None
        dfs(root,0,0)
        # print(HashMap)

        c_min,c_max = float('+inf'), float('-inf')
        r_min,r_max = 0,0
        for k,v in HashMap.items():
            c_min = min(c_min,k[1])
            c_max = max(c_max,k[1])
            r_max = max(r_max,k[0])
        # print(r_max,c_min,c_max)

        res = []

        for c in range(c_min,c_max+1):
            col = []
            for r in range(0,r_max+1):
                if (r,c) in HashMap:
                    col.extend(HashMap[(r,c)])
            res.append(col)

        return res
        
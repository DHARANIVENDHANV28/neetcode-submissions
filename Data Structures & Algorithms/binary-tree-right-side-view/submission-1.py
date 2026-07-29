# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        output = []
        tmp = []
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if tmp:
                output.append(tmp[-1])
                tmp = []
        return output

        
        
        
        
        
        
        
        
        
        
        
        
        
        # output = []
        # def fun(node):
        #     if not node:
        #         return 
        #     output.append(node.val)
        #     return fun(node.right)
        # fun(root)
        # return output
    
        
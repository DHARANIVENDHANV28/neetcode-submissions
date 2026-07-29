# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            current_sum = node.val + left + right
            max_sum = max(max_sum, current_sum)

            return node.val + max(left, right)

        dfs(root)
        return max_sum

# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         # if not root.left and not root.right:
#         #     return root.val 
#         max_sum = float("-inf")
#         def maxsumroute(node):
#             if not node:
#                 return 0
#             return max(node.val+maxsumroute(node.left),node.val+maxsumroute(node.right))
#         def dfs(node):
#             nonlocal max_sum
#             if node.left:
#                 left = node.left  
#             else:
#                 return
#             if node.right: 
#                 right = node.right  
#             else: 
#                 return
#             Sum = maxsumroute(left)+maxsumroute(right)+node.val
#             max_sum = max(max_sum,Sum)
#             dfs(node.left)
#             dfs(node.right)
#         dfs(root)
        
#         return max_sum
        # max_sum = float("-inf")
        # def maxsum(node):
        #     if not node:
        #         return 0
        #     return max(node.val+maxsum(node.left),node.val+maxsum(node.right))
        # def dfs(node):
        #     if not node.left or node.right:
        #         return 
        #     if node.left or node.right:
        #         left = node.left 
        #         right = node.right 
        #         max_sum=max(max_sum,node.val+maxsum(left)+maxsum(right))

        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return max_sum

        
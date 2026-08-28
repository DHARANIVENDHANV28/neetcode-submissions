# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            queue = deque()
            queue.append(root)
            foundNull = False
            while queue:
                node = queue.popleft()
                
                if node:
                    if foundNull:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    foundNull = True
            
            return True
        return bfs(root)



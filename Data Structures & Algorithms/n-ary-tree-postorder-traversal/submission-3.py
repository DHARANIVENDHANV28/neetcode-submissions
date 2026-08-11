"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return None
            for c in node.children:
                dfs(c)
            res.append(node.val)
            # return None
        dfs(root)
        return res
        
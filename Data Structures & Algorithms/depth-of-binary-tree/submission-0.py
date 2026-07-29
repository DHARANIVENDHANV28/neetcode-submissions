# Definition for a binary tree node.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stak = [[root,1]]
        result = 0

        while stak:
            node,depth = stak.pop()

            if node:
                result = max(result,depth)
                stak.append([node.left,depth+1])
                stak.append([node.right,depth+1])

        return result
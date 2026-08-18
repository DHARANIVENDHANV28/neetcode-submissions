class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]

        def left_boundary(node):
            if not node:
                return None
            if not node.left and not node.right:
                return None
            res.append(node.val)
            if node.left:
                left_boundary(node.left)
            else:
                left_boundary(node.right)
            return None
        
        def leaves(node):
            if not node:
                return None
            if not node.left and not node.right:
                res.append(node.val)
                return None
            if node.left:
                leaves(node.left)
            if node.right:
                leaves(node.right)
            return None
        
        def right_boundary(node):
            if not node:
                return None
            if not node.right and not node.left:
                return None

            if node.right:
                right_boundary(node.right)
            else:
                right_boundary(node.left)
            res.append(node.val) 

        left_boundary(root.left)
        leaves(root.left)
        leaves(root.right)
        right_boundary(root.right)
        return res
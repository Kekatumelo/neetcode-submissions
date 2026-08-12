# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
       
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            

        
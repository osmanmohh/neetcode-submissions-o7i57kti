# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        def inorder(root):
            if root is None:
                return True
            left = inorder(root.left)
            if root.val <= self.prev:
                return False
            self.prev = root.val
            right = inorder(root.right)
            return left and right
        return inorder(root)



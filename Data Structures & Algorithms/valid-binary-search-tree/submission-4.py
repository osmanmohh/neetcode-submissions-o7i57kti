# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        res = True
        def inorder(root):
            nonlocal prev, res
            if not root:
                return
            inorder(root.left)
            if prev >= root.val:
                res = False
            prev = root.val
            inorder(root.right)
        inorder(root)
        return res

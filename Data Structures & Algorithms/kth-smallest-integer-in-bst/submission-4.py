# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 1
        res = None
        def dfs(node):
            if not node:
                return
            
            nonlocal index
            nonlocal res
            dfs(node.left)

            if k == index:
                res = node.val
            index += 1
            dfs(node.right)
        dfs(root)
        return res

        
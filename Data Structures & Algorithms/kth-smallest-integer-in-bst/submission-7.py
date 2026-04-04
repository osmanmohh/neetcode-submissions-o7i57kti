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
            nonlocal index
            nonlocal res
            if not node or res is not None:
                return

            dfs(node.left)

            if k == index:
                res = node.val
            index += 1
            dfs(node.right)
        dfs(root)
        return res

        
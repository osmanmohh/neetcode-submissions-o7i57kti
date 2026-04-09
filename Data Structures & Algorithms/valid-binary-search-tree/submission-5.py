# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        prev = float('-inf')

        def dfs(node):
            nonlocal res, prev

            if not node:
                return
            
            dfs(node.left)

            if node.val > prev:


                prev = node.val


            else:
                res = False
            print(res)
            
            dfs(node.right)
        dfs(root)
        return res
        
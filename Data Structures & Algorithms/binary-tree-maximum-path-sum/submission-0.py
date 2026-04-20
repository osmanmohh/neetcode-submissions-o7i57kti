# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def dfs(root):
            if not root:
                return 0
            nonlocal best
            
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            best = max(best, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return best

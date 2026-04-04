# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxSeen):
            if not root:
                return 0
            count = 1 if root.val >= maxSeen else 0
            maxSeen = max(root.val, maxSeen)
            count += dfs(root.left, maxSeen) + dfs(root.right, maxSeen)
            return count
        return dfs(root, float('-inf'))
        

        
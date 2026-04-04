# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heightMap = {None:0}
        def height(node):
            if not node:
                return 0
            
            heightMap[node] =  1 + max(height(node.left), height(node.right))
            return heightMap[node]
        height(root)
        def dfs(node):
            if not node:
                return True
            
            if abs(heightMap[node.left] - heightMap[node.right]) > 1:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
            
            
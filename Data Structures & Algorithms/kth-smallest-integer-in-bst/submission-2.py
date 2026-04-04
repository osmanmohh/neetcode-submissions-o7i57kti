class Solution:
    def kthSmallest(self, root, k):
        count = 0
        res = None
        def inorder(root):
            nonlocal count, res
            if root is None:
                return
            inorder(root.left)
            count += 1

            if count == k:
                res = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return res
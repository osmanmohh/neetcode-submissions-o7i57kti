class Solution:
    def kthSmallest(self, root, k):
        count = 1
        res = None
        def inorder(root):
            nonlocal count, res
            if not root:
                return
            inorder(root.left)
            if count == k:
                res = root.val
            count += 1
            inorder(root.right)

        inorder(root)
        return res
class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.res = root.val
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.count += 1

            if self.count == k:
                self.res = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return self.res
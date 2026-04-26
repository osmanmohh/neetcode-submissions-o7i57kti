class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])
        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        return False
        





        # 8 % cols = c
        # 8 // cols = 2
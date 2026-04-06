class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        l, r = 1, x // 2
        while l <= r:
            m = (l + r) // 2
            prod = m * m
            if prod == x:
                return m
            elif prod < x:
                l = m + 1
            else:
                r = m - 1
        return l - 1
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        def sumSquares(x):
            x = [int(d)*int(d) for d in str(x)]
            return sum(x)
        seen = set()
        while n != 1:
            n = sumSquares(n)
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True

        
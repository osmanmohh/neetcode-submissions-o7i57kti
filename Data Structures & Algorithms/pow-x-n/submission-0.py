class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg, power = n < 0, abs(n)
        res = 1
        for _ in range(power):
            res *= x
        return res if not neg else 1 / res

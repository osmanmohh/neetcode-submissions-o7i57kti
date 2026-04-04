class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 -1 
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        res = sign * int(str(abs(x))[::-1])
        return res if INT_MIN <= res <= INT_MAX else 0
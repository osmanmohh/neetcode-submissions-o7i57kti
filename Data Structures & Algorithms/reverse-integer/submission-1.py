class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:  return 0
        INT_MAX = 2**31 -1 
        INT_MIN = -2**31

        sign = x // abs(x)
        res = sign * int(str(abs(x))[::-1])
        return res if INT_MIN <= res <= INT_MAX else 0
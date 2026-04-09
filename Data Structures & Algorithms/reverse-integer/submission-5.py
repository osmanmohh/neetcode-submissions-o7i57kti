class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = -int(str(-x)[::-1])
        else:
            num = int(str(x)[::-1])
        return num if -2**31 <= num <= 2**31 else 0
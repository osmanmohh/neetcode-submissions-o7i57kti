class Solution:
    def sumOfSquares(self,n):
        digits = [int(d) for d in str(n)]
        return sum(d*d for d in digits)
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num >= 1:
            num = self.sumOfSquares(num)
            if num == 1:
                return True
            if num in seen:
                break
            seen.add(num)

        return False
        
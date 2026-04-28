class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        
        if digits[-1] <= 9:
            return digits
        
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + carry
            digit = val % 10
            carry = val // 10
            digits[i] = digit
        if carry:
            digits = [1] + digits
        return digits
        

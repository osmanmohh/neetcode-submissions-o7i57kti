class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i, num in enumerate(digits[::-1]):
            res += 10**i * num
        res += 1
        return [int(c) for c in str(res)] 

        
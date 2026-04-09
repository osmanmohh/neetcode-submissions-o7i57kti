class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr = 0
        for num in nums:
            curr = curr + 1 if num else 0
            best = max(best, curr)
            
        return best
        
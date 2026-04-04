class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        maxIndex = 0
        for i in range(len(nums)):
             if maxIndex < i:
                return False
             maxIndex = max(nums[i] + i, maxIndex)
           
        return True
        
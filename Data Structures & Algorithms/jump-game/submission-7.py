class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1
        maxIndex = 0
        for i in range(len(nums)):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + nums[i])

            if maxIndex >= target:
                return True
        return False
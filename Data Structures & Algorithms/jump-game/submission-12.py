class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        farthest = 0
        for i, num in enumerate(nums):
            if farthest >= target:
                return True
            farthest = max(farthest, num + i)
            if farthest == i:
                return False
        return False

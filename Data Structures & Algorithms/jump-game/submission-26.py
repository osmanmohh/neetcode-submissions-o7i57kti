class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        target = len(nums) - 1
        if len(nums) == 1:
            return True
        for i in range(target):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)
            if farthest >= target:
                return True
        return False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        target = len(nums) - 1
        for i in range(len(nums) - 1):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= target:
                return True

        return farthest >= target
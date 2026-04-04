class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        def f(i, remaining):
            if remaining == 0:
                return True
            if i == len(nums):
                return False
            if remaining < 0:
                return False
            return f(i + 1, remaining) or f(i+1, remaining - nums[i])
        return f(0, target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        def f(i, rest):
            if rest == 0:
                return True
            if i == len(nums):
                return False
            if rest < 0:
                return False
            return f(i+1, rest) or f(i+1, rest - nums[i])
        return f(0, total // 2)
        
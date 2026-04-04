class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        memo = {}
        def f(i, rest):
            if rest == 0:
                return True
            if i == len(nums):
                return False
            if rest < 0:
                return False
            if (i, rest) in memo:
                return memo[(i, rest)]

            memo[(i, rest)] = f(i+1, rest) or f(i+1, rest - nums[i])
            return memo[(i, rest)]
        return f(0, total // 2)
        
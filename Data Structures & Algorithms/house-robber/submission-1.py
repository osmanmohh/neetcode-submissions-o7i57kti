class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def f(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + f(i + 2), f(i + 1))
            return memo[i]
        return f(0)

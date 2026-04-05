class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(i, memo={}):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = max(nums[i] + f(i + 2), f(i + 1))
            return memo[i]
        
        return f(0)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robLinear(nums):
            memo = {}
            def f(i):
                if i in memo:
                    return memo[i]
                if i >= len(nums):
                    return 0
                memo[i] = max(f(i + 1), nums[i] + f(i + 2))
                return memo[i]
            return f(0)
        return max(robLinear(nums[1:]), robLinear(nums[:-1]))
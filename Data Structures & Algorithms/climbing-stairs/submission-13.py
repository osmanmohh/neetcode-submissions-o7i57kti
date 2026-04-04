class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1  # one way to stay at the bottom
        dp[1] = 1  # one way to take a single step
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

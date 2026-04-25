class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1: 1, 2:1}

        def f(n):
            if n in memo:
                return memo[n]
            memo[n] = f(n - 3) + f(n - 2) + f(n - 1)
            return memo[n]
        return f(n)
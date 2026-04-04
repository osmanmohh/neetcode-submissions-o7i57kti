class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def f(a):
            if a in memo:
                return memo[a]
            if a < 0:
                return float('inf')
            best = float('inf')
            for c in coins:
                best = min(f(a - c) + 1, best)
            memo[a] = best
            return memo[a]
        res = f(amount)
        return res if res != float('inf') else -1
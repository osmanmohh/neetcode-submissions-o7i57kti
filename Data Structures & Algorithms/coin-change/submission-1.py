class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return float('inf')
            best = float('inf')
            for c in coins:
                best = min(best, dfs(amount - c) + 1)
                memo[amount] = best
            return memo[amount]
        res = dfs(amount)
        return res if res != float('inf') else -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def dfs(a):
            if a in memo:
                return memo[a]
            if a < 0:
                return float('inf')
            best = float('inf')
            for c in coins:
                best = min(best, dfs(a - c) + 1)
            
            memo[a] = best
            return memo[a]
        
        best = dfs(amount)
        return best if best != float('inf') else -1
        
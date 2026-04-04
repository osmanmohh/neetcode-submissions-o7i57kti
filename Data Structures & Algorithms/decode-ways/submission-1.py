class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {n:1}
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            memo[count] = dfs(i + 1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                memo[count] += dfs(i + 2)
            return memo[count]
        return dfs(0)
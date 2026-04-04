class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {n:1} # base case, 1 way to decode 
        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            count = dfs(i + 1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                count += dfs(i + 2)
            memo[i] = count

            return count
        return dfs(0)

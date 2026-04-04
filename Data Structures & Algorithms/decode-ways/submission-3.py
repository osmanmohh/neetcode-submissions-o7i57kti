class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        count = 0
        def dfs(i):
            nonlocal count
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            count = dfs(i + 1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                count += dfs(i + 2)
            return count
        dfs(0)
        return count
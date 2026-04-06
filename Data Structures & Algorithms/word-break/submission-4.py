class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    memo[i] = dfs(j+1)
                    if memo[i]:
                        return True
            return False
        return dfs(0)

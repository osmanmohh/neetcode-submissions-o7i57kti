class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        def isPal(l, r):
            if l >= r:
                return True
            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = (s[l] == s[r] and isPal(l + 1, r - 1))
            return memo[(l, r)]
        best = ""
        for l in range(len(s)):
            for r in range(l, len(s)):
                if s[l] == s[r] and isPal(l, r):
                    if (r - l + 1) > len(best):
                        best = s[l:r+1]
        return best
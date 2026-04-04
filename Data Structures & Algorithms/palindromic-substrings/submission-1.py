class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def isPal(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l >= r:
                return True
            memo[(l, r)] = s[l] == s[r] and isPal(l+1, r-1)
            return memo[(l, r)]
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPal(i, j):
                    count += 1
        return count

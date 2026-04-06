class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = [0, 0]
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > best[1] - best[0]:
                    best = (l, r)
                l -= 1
                r += 1

                
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > best[1] - best[0]:
                    best = (l, r)
                l -= 1
                r += 1

        [l, r] = best
        return s[l:r+1]
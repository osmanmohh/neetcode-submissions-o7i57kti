class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        if len(s) > len(t):
            return False
        
        n = len(s)
        i = 0
        j = 0
        while i < n and j < len(t):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j < len(t) and s[i] == t[j]:
                i += 1
            j+=1
        
        return i == n
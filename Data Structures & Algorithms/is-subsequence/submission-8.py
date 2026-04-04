class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        if len(s) > len(t):
            return False
        
        n = len(s)
        i = 0
        j = 0
        res = []

        while i < n and j < len(t):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j < len(t) and s[i] == t[j]:
                print(i, j)
                res.append(t[j])
                i += 1
            j+=1
        
        res = ''.join(res)
        print(res)
        return res == s
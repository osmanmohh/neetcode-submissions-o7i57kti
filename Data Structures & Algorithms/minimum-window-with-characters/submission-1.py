from collections import Counter, defaultdict
class Solution:
    def isSubstring(self, sCount, tCount): # O(keys)
        return all(sCount[char] >= tCount[char] for char in tCount) 
    
    def minWindow(self, s: str, t: str) -> str: 
        if len(t) > len(s):
            return ""
        tCount = Counter(t)
        sCount = Counter(s[:len(t)])
        if self.isSubstring(sCount, tCount):
            return s[:len(t)]

        best = None
        l = 0
        for r in range(len(t), len(s)):
            sCount[s[r]] += 1
            print(s[l:r+1])
            
            while self.isSubstring(sCount, tCount):
                if not best or r - l < best[1] - best[0]:
                    best = (l, r)
                sCount[s[l]] -= 1
                if not sCount[s[l]]:
                    del sCount[s[l]]
                l += 1
        
        if not best:
            return ""
        (l, r) = best

        return s[l:r+ 1] 
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Map = Counter(s1)
        k = len(s1)
        s2Map = Counter(s2[:k])
        if s2Map == s1Map:
            return True
        
        l = 0
        for r in range(k, len(s2)):
            s2Map[s2[r]] += 1
            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                del s2Map[s2[l]]
            if s2Map == s1Map:
                return True
            l += 1
        return False
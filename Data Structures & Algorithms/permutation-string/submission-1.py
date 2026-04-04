class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Map, s2Map = {}, {}
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) + 1
        
        for i in range(len(s1)):
            s2Map[s2[i]] = s2Map.get(s2[i], 0) + 1
        
        if s2Map == s1Map:
                return True
                
        for i in range(len(s1), len(s2)):
            startChar = s2[i - len(s1)]
            endChar = s2[i]

            s2Map[startChar] -= 1
            if s2Map[startChar] == 0:
                del s2Map[startChar]

            s2Map[endChar] = s2Map.get(endChar, 0) + 1

            if s2Map == s1Map:
                return True

        return False
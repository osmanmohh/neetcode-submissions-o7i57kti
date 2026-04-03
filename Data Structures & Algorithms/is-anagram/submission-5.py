class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        count = [0] * 26
        for i in range(n):
            count[ord('a') - ord(s[i])] += 1
            count[ord('a') - ord(t[i])] -= 1
        
        return all(i == 0 for i in count)


        
        
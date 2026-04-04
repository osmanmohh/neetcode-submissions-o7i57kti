class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0
        currLen = 0
        l = 0
        for r in range(len(s)):
            print(seen)
            while s[r] in seen:
               
                seen.remove(s[l])
                l += 1
                currLen -= 1
            seen.add(s[r])
            currLen += 1
            maxLen = max(maxLen, currLen)
        return maxLen
            


       
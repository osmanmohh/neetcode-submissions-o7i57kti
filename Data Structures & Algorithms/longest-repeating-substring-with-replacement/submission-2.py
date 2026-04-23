from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window is valid if there are no repeating chars, with at most k violations
        count = defaultdict(int)
        maxLen = 0
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq,count[s[r]])
            while (r - l + 1)  - k> maxFreq:
                count[s[l]] -= 1
                maxFreq = max(maxFreq,count[s[l]])
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        maxf = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                maxf = max(maxf, freq[s[l]])
                l += 1
        return (r - l + 1)
    
            
            
            

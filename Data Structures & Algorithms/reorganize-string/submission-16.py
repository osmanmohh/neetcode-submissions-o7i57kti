from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        arr = sorted(s)
        res = [""] * len(s)
        i = 0
        for char, freq in sorted(counts.items(), key=lambda x: -x[1]):
            for _ in range(freq):
                if i >= len(s):
                    i = 1
                res[i] = char
                i += 2
            
        return "".join(res)

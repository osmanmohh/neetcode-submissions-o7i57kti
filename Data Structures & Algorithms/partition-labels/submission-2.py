class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        res = []
        start = 0
        lastIdx = 0
        for i, char in enumerate(s):
            lastIdx = max(lastIdx, last[char])
            if lastIdx == i:
                print(s[start:i+1])
                res.append(i +1 - start)
                start = i+1
        return res
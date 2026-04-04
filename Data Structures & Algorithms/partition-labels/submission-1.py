class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        res = []
        currEnd = 0
        size = 0
        for i, c in enumerate(s):
            currEnd = max(currEnd, last[c])
            size += 1
            if currEnd == i:
                res.append(size)
                size = 0
        return res

            

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = collections.Counter(s)
        res = []
        for char in order:
            res.extend(char * cnt[char])
            del cnt[char]
        
        for char in cnt:
            res.extend(char * cnt[char])
        return ''.join(res)

        
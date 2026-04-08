class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(len(s) for s in strs)
        target = strs[0]
        res = 0
        i = 0
        while i < n and all(s[i] == target[i] for s in strs):
            res += 1
            i += 1
        return target[:res]

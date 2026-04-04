class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(len(s) for s in strs)
        res = 0
        target = strs[0]
        for i in range(n):
            if all(s[i] == target[i] for s in strs[1:]):
                res += 1
            else:
                return target[:res]
        return target[:res]
            
       
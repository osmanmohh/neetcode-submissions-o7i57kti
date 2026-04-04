class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(len(s) for s in strs)
        target = strs[0]
        for i in range(n):
            if not all(s[i] == target[i] for s in strs[1:]):
                return target[:i]
        
        return target[:n]
            
       
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        good = set(allowed)
        res = 0
        for word in words:
            if all(char in good for char in word):
                res += 1
        return res
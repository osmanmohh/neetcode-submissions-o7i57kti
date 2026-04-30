class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        seen = set(words)
        res = []
        for word in words:
            if any(word in word2 for word2 in seen if word2 != word):
                res.append(word)
        return res
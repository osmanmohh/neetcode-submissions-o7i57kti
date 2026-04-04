class Solution:
#   ["Breaking", "Bad"] -> "8|Breaking3|Bad"
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}|{s}" for s in strs)

#   "8|Breaking3|Bad" -> ["Breaking", "Bad"] 
    def decode(self, s: str) -> List[str]:
        res = []
        num = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c != "|":
                num += c
                i += 1
                continue
            length = int(num)
            word = s[i + 1: i + length + 1]
            res.append(word)
            i += length + 1
            num = ""
        return res

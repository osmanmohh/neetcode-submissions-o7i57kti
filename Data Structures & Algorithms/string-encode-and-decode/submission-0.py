class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '|')
            for c in s:
                res.append(c)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            num = ""
            while c != '|':
                num += c
                i+=1
                c = s[i]
            print(num)
            
            num = int(num)
            res.append(s[i+1:i+num+1])
            i += num + 1
        return res
        
            




"""
["Hello","World"]
5|Hello5|World
"""
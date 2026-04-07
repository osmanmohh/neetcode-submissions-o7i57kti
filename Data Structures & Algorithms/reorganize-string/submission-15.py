from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        arr = sorted(s)
        mid = (len(arr) + 1) // 2
        s1 = arr[:mid]
        s2 = arr[mid:]

        def interleave(a, b):
            res = []
            i = j = 0
            turn_a = True

            while i < len(a) or j < len(b):
                if turn_a:
                    if i < len(a):
                        res.append(a[i])
                        i += 1
                    elif j < len(b):
                        res.append(b[j])
                        j += 1
                else:
                    if j < len(b):
                        res.append(b[j])
                        j += 1
                    elif i < len(a):
                        res.append(a[i])
                        i += 1
                turn_a = not turn_a

            ans = ''.join(res)
            for k in range(1, len(ans)):
                if ans[k] == ans[k - 1]:
                    return ""
            return ans

        ans = interleave(s1, s2)
        if ans:
            return ans
        return interleave(s2, s1)
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            m = (l + r) // 2
            k = m
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            if total <= h:
                best = min(best, k)
                r = m - 1
            else:
                l = m + 1
        return best


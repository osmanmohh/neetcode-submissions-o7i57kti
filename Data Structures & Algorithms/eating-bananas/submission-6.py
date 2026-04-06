import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            k = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            print(k, total)
            if total <= h:
                r = k - 1
                best = min(best, k)
            else:
                l = k + 1
        return best
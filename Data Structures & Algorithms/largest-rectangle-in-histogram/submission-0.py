class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n):
            minHeight = heights[i]
            curr = best = 0
            for h in heights:
                if h >= minHeight:
                    curr += 1
                else:
                    curr = 0
                best = max(best, curr)
            res = max(res, minHeight * best)
        return res
        
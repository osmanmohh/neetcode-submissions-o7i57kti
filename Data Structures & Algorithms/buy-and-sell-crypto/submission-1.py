class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minSeen = float('inf')
        for p in prices:
            minSeen = min(minSeen, p)
            maxProfit = max(maxProfit, p - minSeen)
        return maxProfit
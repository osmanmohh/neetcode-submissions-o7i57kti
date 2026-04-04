import heapq
import collections
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        best = defaultdict(int)
        for xi, yi in zip(x, y):
            best[xi] = max(best[xi], yi)
        if len(best) < 3:
            return -1
        
        heap = []
        for val in best.values():
            heapq.heappush(heap, val)
            if len(heap) > 3:
                heapq.heappop(heap)
        
        return sum(heap)
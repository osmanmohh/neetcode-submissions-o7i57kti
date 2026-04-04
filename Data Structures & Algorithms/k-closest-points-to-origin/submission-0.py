import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(p):
            return (math.sqrt(p[0]**2 + p[1] ** 2))
        heap = []
        for point in points:
            heapq.heappush(heap, (-dis(point), point))
            if len(heap) > k:
                heapq.heappop(heap)
        return[p for _ , p in heap]
        
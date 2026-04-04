import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = lambda p: p[0] ** 2 + p[1] ** 2
        heap = []
        for p in points:
            heapq.heappush(heap, (-dis(p),p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [p for _, p in heap]
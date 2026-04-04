class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(heap, -(y - x) )
            else:
                heapq.heappush(heap,  -(x - y) )
        return -heap[0] if heap else 0


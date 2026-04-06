import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-num,i) for i, num in enumerate(nums[:k])]
        heapq.heapify(heap)
        res = [-heap[0][0]]
        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l += 1
            while not l <= heap[0][1] <= r:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res


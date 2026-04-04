import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(heap)
        res = [-heap[0][0]]
        l = 0
        for r in range(k, len(nums)):
            l += 1
            heapq.heappush(heap, (-nums[r], r))

            (val, index) = heap[0]
            val = -val
            while not (l <= index <= r):
                (val, index) = heapq.heappop(heap)
                val = -val
            res.append(val)

            heapq.heappush(heap, (-val, index))

        return res
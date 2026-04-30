import heapq
class MedianFinder:
    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.left or num >= self.left[0]:
            heapq.heappush(self.left, num)
        else:
            heapq.heappush_max(self.right, num)
        
        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left)
            heapq.heappush_max(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop_max(self.right)
            heapq.heappush(self.left, val)

        

    def findMedian(self) -> float:
        print(self.left)
        print(self.right)
        print()
        if len(self.left) > len(self.right):
            return self.left[0]
        else:
            return (self.left[0] + self.right[0]) / 2
        
        
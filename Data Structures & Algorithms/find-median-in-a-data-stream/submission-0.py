import heapq
class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
    
        if len(self.low) - 1 > len(self.high):
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)
      
    def findMedian(self) -> float:
       
        if (len(self.low) + len(self.high)) % 2:
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2
       
        
        
from collections import defaultdict
import heapq
class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.heap = []
        self.index = 0
        

    def push(self, val: int) -> None:
        self.counter[val] += 1
        heapq.heappush_max(self.heap, (self.counter[val], self.index, val))
        self.index += 1        

    def pop(self) -> int:
        (freq, idx, val) = heapq.heappop_max(self.heap)
        self.counter[val] -= 1
        return val




        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
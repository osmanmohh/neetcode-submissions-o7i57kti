class MinStack:

    def __init__(self):
        self.stack = [] # (val, minSeen)
        self.minSeen = float('inf')
    def push(self, val: int) -> None:
        self.minSeen = min(self.minSeen, val)
        self.stack.append((val, self.minSeen))


    def pop(self) -> None:
        (val, _) = self.stack.pop()
        if val == self.minSeen:
            self.minSeen = self.getMin() if self.stack else float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


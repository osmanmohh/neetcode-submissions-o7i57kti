class MinStack:

    def __init__(self):
        self.stack = [] # (val, minSeen)
    def push(self, val: int) -> None:
        currMin = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, currMin))


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


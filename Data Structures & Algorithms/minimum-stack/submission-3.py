class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.getMin():
            self.minStack.append(val)
        

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.getMin():
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

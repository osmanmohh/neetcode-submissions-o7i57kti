class Solution:
    def eval(self, a, b, token):
        a, b = int(a), int(b)
        res = None
        match token:
            case "+":
                res = a + b
            case "-":
                res =  a - b
            case "*":
                res =  a * b
            case "/":
                res =  int(a / b)

        return res


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                stack.append(t)
                continue
            b, a = stack.pop(), stack.pop()
            val = self.eval(a, b, t)
            stack.append(val)
        return int(stack[-1])


                             
        
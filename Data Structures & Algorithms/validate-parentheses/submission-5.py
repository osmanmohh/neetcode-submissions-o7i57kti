class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            '}' : '{',
            ')' : '('
        }
        openParens = pairs.values()
        stack = []
        for token in s:
            if token in openParens:
                stack.append(token)
            else:
                if not stack or stack[-1] != pairs[token]:
                    return False
                else:
                    stack.pop()
        return not stack

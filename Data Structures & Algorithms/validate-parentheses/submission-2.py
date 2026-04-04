class Solution:

  def isValid(self, s: str) -> bool:
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }


    open = pairs.values()
    closed = pairs.keys()
    stack = []
    for paren in s:
        if paren in open:
            stack.append(paren)
        else:
            if not stack or stack[-1] != pairs[paren]:
                return False
            else:
                stack.pop()
    return not stack



#([{}])



"""

{
[
(
"""
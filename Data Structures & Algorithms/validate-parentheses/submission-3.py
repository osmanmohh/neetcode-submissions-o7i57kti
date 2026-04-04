class Solution:

  def isValid(self, s: str) -> bool:
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }


    stack = []
    for paren in s:
        if paren in pairs.values(): # open paren
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
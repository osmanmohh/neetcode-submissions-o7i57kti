class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n     # can also store distances/indices depending on problem
        stack = []         # stores indices
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
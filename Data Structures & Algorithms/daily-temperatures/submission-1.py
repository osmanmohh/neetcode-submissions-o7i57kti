class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n     # can also store distances/indices depending on problem
        stack = []         # stores indices
        for i, num in enumerate(temperatures):
            while stack and stack[-1][1] < num:
                j = stack.pop()[0]
                res[j] = i - j
            stack.append((i, num))
        return res
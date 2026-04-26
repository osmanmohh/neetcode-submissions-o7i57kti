class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][0]:
                stack.append((temp, i))
                continue
            while stack and temp > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))

        
        return res
        
        

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
      
        result = []


        def backtrack(current):
            if len(current) == n:
                result.append(list(current))
                return
            
            for i in range(n):
                if used[i]:
                    continue
                current.append(nums[i])
                used[i] = True
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])
        return result

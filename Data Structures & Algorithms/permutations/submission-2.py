class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        
        result = []

        def backtrack(current):

            if len(current) == len(nums):
                result.append(list(current))

            for i in range(len(nums)):
                # 2a. Constraints — skip duplicates
                if used[i]:
                    continue
                

                current.append(nums[i])
                used[i] = True

                # 2c. Recurse
                backtrack(current)

                # 2d. Undo choice (backtrack)
                current.pop()
                used[i] = False


        backtrack([])
        return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)  # ✅ Declare once
        result = []

        def backtrack(current):
            # 1. Base case — record current subset
            if len(current) == len(nums):
                result.append(list(current))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # 2b. Make choice
                current.append(nums[i])
                used[i] = True

                # 2c. Recurse
                backtrack(current)

                # 2d. Undo choice (backtrack)
                current.pop()
                used[i] = False

        backtrack([])
        return result

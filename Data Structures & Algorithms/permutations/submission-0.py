class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(current, seen):
            # 1. Base case — record current subset
            if len(current) == len(nums):
                result.append(list(current))
                return

            for num in nums:
                if num in seen:
                    continue

                # 2b. Make choice
                current.append(num)
                seen.add(num)

                # 2c. Recurse
                backtrack(current, seen)

                # 2d. Undo choice (backtrack)
                current.pop()
                seen.remove(num)

        result = []
        seen = set()
        backtrack([], seen)
        return result

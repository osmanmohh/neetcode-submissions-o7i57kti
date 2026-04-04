class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        candidates = [num for num in candidates if num <= target]
        def backtrack(start, current, currSum):
            # 1. Base case — record current subset
            if currSum == target:
                result.append(list(current))

            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                current.append(candidates[i])
                currSum += candidates[i]

                # 2c. Recurse
                backtrack(i + 1, current, currSum)

                # 2d. Undo choice (backtrack)
                current.pop()
                currSum -= candidates[i]


        backtrack(0, [], 0)
        return result
        
        
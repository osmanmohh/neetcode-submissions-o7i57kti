class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      
        result = []
        candidates.sort()

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                total += candidates[i]
                backtrack(i + 1, current, total)
                total -= current.pop()

        backtrack(0, [], 0)
        return result

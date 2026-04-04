class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(start, current):
            result.append(list(current))
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result

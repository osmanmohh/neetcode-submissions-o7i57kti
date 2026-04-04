class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(start, current, currSum):
            if currSum == target:
                result.append(list(current))
            
            if currSum > target:
                currSum = 0
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                currSum += nums[i]
                backtrack(i, current, currSum)
                currSum -= current.pop()

        backtrack(0, [], 0)
        return result

        
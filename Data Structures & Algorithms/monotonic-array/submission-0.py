class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # increasing
        isIncreasing = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                isIncreasing = False
        if isIncreasing:
            return True

        isDecreasing = True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                isDecreasing = False
        return isDecreasing
        
class Solution:
    def check(self, nums: List[int]) -> bool:
        minIdx = 0
        for i, num in enumerate(nums):
            if num < nums[minIdx]:
                minIdx = i
        
        prev = float('-inf')
        for i in range(minIdx, len(nums)):
            if nums[i] < prev:
                return False
            prev = nums[i]
        
        for i in range(minIdx):
            if nums[i] < prev:
                return False
            prev = nums[i]
        return True
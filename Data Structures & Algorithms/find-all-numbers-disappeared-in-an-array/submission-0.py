class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        return [i+1 for i, num in enumerate(nums) if num > 0]
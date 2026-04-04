class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for r in range(len(nums) // 2, len(nums)):
            if nums[l] == nums[r]:
                return nums[l]
            l += 1
        
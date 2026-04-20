class Solution:
    def check(self, nums):
        descents = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                descents += 1
        return descents <= 1
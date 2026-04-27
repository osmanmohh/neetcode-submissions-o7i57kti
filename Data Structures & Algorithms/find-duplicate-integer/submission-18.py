class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            idx = abs(num) - 1
            if nums[idx] < 0:
                return idx + 1
            nums[idx] = -abs(nums[idx])
            print(nums)
        
        for num in nums:
            if num > 0:
                return num
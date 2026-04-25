class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res[0] = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
       
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res[1] = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return res

        
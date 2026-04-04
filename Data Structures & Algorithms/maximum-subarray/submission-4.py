class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]
        for num in nums[1:]:
            if curr < 0:
                curr = 0
            curr += num
           
            best = max(best, curr)
           
        return best


        # [2,-3,4,-2,2,1,-1,4]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n - 1):
            l, r = i + 1, n - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    res.add(tuple(sorted((nums[i], nums[l], nums[r]))))
                    l += 1
                    r -= 1 
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1
        return list(res)



        
        
        
        

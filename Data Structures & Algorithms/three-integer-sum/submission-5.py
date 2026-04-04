class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            l, r = i+1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        print(res)
        return list(set(res))
                

        
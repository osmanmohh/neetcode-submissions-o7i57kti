class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 2):
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return list(res)

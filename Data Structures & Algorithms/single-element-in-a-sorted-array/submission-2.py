class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if 0 < m < len(nums) - 1:
                if nums[m + 1] == nums[m]:
                    if (len(nums) - m) % 2 == 0:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m - 1] == nums[m]:
                    if m % 2 == 1:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    return nums[m]
        return nums[l]
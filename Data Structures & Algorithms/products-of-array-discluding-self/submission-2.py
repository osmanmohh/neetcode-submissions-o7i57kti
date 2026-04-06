class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for num in nums[:-1]:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in reversed(nums[1:]):
            suffix.append(suffix[-1] * num)

        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[n - i - 1]

        return res
        
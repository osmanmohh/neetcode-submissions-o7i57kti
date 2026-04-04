class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])
        print(prefix)
        minVal = float('inf')
        res = nums[0]
        for num in prefix:
            res = max(res, num - minVal)
            minVal = min(minVal, num)

        return res
     
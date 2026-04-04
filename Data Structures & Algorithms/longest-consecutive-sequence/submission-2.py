class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxx = 0
        for num in nums:
            if num - 1 not in seen:
                curr = 0
                i = 0
                while num + i in seen:
                    curr += 1
                    i += 1
                maxx = max(maxx, curr)
        return maxx

        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        maxLen = 1
        for num in nums:
            currLen = 1

            if num - 1 not in nums:
                curr = num
                while curr + 1 in nums:
                    currLen += 1
                    curr += 1
                maxLen = max(maxLen, currLen)
        return maxLen
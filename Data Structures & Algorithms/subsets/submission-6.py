class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def bactrack(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            bactrack(i + 1)
            curr.pop()
            bactrack(i + 1)
        bactrack(0)
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def f(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            f(i + 1)
            curr.pop()
            f(i + 1)
        f(0)
        return res
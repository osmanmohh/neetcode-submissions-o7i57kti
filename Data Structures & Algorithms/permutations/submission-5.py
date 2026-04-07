class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False] * n
        def dfs(curr):
            if len(curr) == n:
                res.append(curr[:])
            for i in range(n):
                if used[i]:
                    continue
                curr.append(nums[i])
                used[i] = True
                dfs(curr)
                curr.pop()
                used[i] = False
            return res


        return dfs([])
        
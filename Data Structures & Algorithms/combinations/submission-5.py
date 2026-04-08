class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        curr = []
        def dfs(i, curr):
            if i >= n:
                if len(curr) == k:
                    res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
            return res
        return dfs(0, [])
        
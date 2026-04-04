class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        farthest = 0
        for i, num in enumerate(nums):
            farthest = max(farthest, num + i)
            print(f'f: {farthest}.  num: {num}.  i: {i}')
            if farthest >= target:
                return True
            if i >= farthest:
                return False
        return False


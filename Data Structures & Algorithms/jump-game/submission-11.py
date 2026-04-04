class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        farthest = 0
        for i, num in enumerate(nums):
            if farthest >= target:
                return True
            farthest = max(farthest, num + i)
            print(f'f: {farthest}   num: {num}')
            if farthest == i:
                return False
        return False

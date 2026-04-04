class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        farthest = 0
        currEnd = 0
        jumps = 0
        for i in range(len(nums) - 1):
           
            farthest = max(farthest, nums[i] + i)
            if i == currEnd:
                currEnd = farthest
                jumps += 1
                        
        return jumps

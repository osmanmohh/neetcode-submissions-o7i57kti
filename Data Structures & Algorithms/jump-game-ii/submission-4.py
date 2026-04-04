class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        currEnd = 0
        jumps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i]) # 5
            if i == currEnd:
                jumps += 1 # 2
                currEnd = farthest # 3

        return jumps
    

"""


"""
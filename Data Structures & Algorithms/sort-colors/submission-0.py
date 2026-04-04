class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]
        for x in nums:
            count[x] += 1
        (zeros, ones, twos) = count
        i = 0
        while zeros:
            nums[i] = 0
            i += 1
            zeros -= 1
        while ones:
            nums[i] = 1
            i += 1
            ones -= 1
        while twos:
            nums[i] = 2
            i += 1
            twos -= 1
    
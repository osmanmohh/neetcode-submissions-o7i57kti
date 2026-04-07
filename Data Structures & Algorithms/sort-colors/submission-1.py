class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for num in nums:
            count[num] += 1
        i = 0
        for j in range(3):
            while count[j]:
                nums[i] = j
                count[j] -= 1
                i += 1
                
        


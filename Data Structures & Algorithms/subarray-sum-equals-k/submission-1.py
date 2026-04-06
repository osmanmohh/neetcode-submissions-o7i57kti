class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        seen = collections.defaultdict(int)
        seen[0] = 1
        count = 0
        for num in nums:
            prefix += num
            if prefix - k in seen:
                count += seen[prefix - k]
            seen[prefix]+=1
            
        return count    
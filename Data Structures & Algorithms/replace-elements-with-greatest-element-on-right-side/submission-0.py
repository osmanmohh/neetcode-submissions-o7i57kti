class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSeen = arr[-1]
        res = arr[:]
        for i in range(len(arr) - 2, -1, -1):
            res[i] = maxSeen
            maxSeen = max(maxSeen, arr[i])

        res[-1] = -1
        return res
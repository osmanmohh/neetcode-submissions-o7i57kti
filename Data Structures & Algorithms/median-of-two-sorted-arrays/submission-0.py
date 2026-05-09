class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = sorted(nums1 + nums2)
        mid = (len(nums1) + len(nums2)) // 2
        return res[mid] if len(res) % 2 else (res[mid] + res[mid - 1]) /2 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = collections.Counter(arr)
        candidates = [char for char in count if count[char] == 1]
        return candidates[k - 1] if len(candidates) >= k else ""
        
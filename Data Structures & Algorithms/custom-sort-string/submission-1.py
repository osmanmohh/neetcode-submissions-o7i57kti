class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = collections.defaultdict(int)
        for i, char in enumerate(order):
            orderMap[char] = i + 1
        return ''.join(sorted(s, key=lambda x: orderMap[x]))
        
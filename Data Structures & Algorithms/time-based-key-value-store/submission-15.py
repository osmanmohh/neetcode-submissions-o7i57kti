from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list) # key -> [(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        arr = self.timeMap[key]
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                l = m + 1
                res = arr[m][1]
            elif arr[m][0] > timestamp:
                r = m - 1

        return res
        

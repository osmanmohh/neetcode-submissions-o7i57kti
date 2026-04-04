class TimeMap:

    def __init__(self):
        self.keyStore = {}

        [1,2,3,4,5,6]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res, arr = "", self.keyStore.get(key, [])
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
       
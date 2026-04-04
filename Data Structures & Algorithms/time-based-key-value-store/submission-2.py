class TimeMap:

    def __init__(self):
        self.keyStore = {}

     

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []

            self.keyStore[key].append((timestamp, value))
        else:
            self.keyStore[key].append((timestamp, value))
     

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        vals = self.keyStore[key]
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        
       
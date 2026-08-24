class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        try:
            a = self.d[key]
        except KeyError:
            return ""

        l, r, c_i = 0, len(a) - 1 , None

        while l <= r:
            m = (l + r) // 2
            t = a[m][0]

            if t <= timestamp:
                c_i = m
                l = m + 1
            else:
                r = m - 1

        return a[c_i][1] if c_i is not None else ""

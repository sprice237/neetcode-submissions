import heapq
import math

def distance_from_origin(point):
    x, y = point
    return math.sqrt(x ** 2 + y ** 2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for p in points:
            heapq.heappush(h, (distance_from_origin(p), p))

        l = []

        for i in range(k):
            l.append(heapq.heappop(h)[1])

        return l
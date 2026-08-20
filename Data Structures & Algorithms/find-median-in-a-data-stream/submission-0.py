import heapq

class MedianFinder:

    def __init__(self):
        # maxheap, so inverted
        self.small_heap = []

        self.big_heap = []

    def addNum(self, num: int) -> None:
        if not self.small_heap and not self.big_heap:
            heapq.heappush(self.big_heap, num)
            return

        if num >= self.big_heap[0]:
            heapq.heappush(self.big_heap, num)
            if len(self.big_heap) == len(self.small_heap) + 2:
                heapq.heappush(self.small_heap, heapq.heappop(self.big_heap) * -1)
        else:
            heapq.heappush(self.small_heap, num * -1)
            if len(self.small_heap) == len(self.big_heap) + 2:
                heapq.heappush(self.big_heap, heapq.heappop(self.small_heap) * -1)
        

    def findMedian(self) -> float:
        if not self.small_heap:
            if not self.big_heap:
                return None
            return self.big_heap[0]
        elif not self.big_heap:
            return self.small_heap[0] * -1

        if len(self.small_heap) > len(self.big_heap):
            return self.small_heap[0] * -1
        elif len(self.big_heap) > len(self.small_heap):
            return self.big_heap[0]
        else:
            return (self.small_heap[0] * -1 + self.big_heap[0]) / 2
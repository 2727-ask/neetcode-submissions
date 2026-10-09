class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
        topMax = -self.maxheap[0] if self.maxheap else float("inf")
        if(num <= topMax):
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if(len(self.minheap) == len(self.maxheap)):
            return (self.minheap[0] + -self.maxheap[0]) / 2
        elif(len(self.minheap) > len(self.maxheap)):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        
        
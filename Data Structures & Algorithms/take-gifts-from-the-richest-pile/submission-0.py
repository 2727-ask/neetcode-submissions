import heapq
from math import isqrt

class Solution:
    def pickGifts(self, gifts, k):
        heap = []
        for x in gifts:
            heap.append(-1 * x)

        heapq.heapify(heap)
        x = 0
        while(x < k):
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -isqrt(largest))
            x = x + 1
            
        return -sum(heap)
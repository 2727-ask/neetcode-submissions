class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [num * -1 for num in nums]
        self.k = k
        heapq.heapify(self.heap)
       

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -1 * val)
        res = heapq.nsmallest(self.k, self.heap)
        print(res, self.k)
        return -1 * res[-1]
        

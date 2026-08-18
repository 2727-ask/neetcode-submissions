class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [-num for num in nums]
        heapq.heapify(res)
        return -heapq.nsmallest(k, res)[-1]

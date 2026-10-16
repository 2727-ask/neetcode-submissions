class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        _map = defaultdict(int)
        heap = []

        for n in nums:
            _map[n] = _map[n] + 1

        for key, val in _map.items():
            heapq.heappush(heap, (-val, key))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
        
        



        
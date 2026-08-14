class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [0 for x in range(k)]
        d = Counter(nums)
        buckets = [[] for x in range(len(nums)+1)]
        for x, y in d.items():
            buckets[y].append(x)
        res = []
        for x in range(len(buckets)-1, 0, -1):
            if(len(res) == k):
                return res
            for y in buckets[x]:
                res.append(y)
        return res
            
                

            

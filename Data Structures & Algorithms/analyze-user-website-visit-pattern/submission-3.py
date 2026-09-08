class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        

        pairs = sorted(zip(timestamp, username, website))

        store = defaultdict(list)
        patterns = defaultdict(int)
        for timestamp, user, page in pairs:
            store[user].append(page)

        for key, val in store.items():
            seen = set(combinations(val, 3))
            for pattern in seen:
                patterns[pattern] = patterns[pattern] + 1
        
        maximum = max(patterns.values())
        heap = []

        for key, val in patterns.items():
            if val == maximum:
                heapq.heappush(heap, key)

        return list(heapq.heappop(heap))



        
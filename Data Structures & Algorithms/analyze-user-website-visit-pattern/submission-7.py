class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        

        usermap = defaultdict(list)
        patternmap = defaultdict(int)


        triples = sorted(zip(timestamp, username, website))

        for timestamp, username, websites in triples:
            usermap[username].append(websites)

        for username, sites in usermap.items():
            combination = set(combinations(sites, 3))
            for pattern in combination:
                patternmap[pattern] = patternmap[pattern] + 1
        

        heap = []
        for pattern, freq in patternmap.items():
            heapq.heappush(heap, (-freq, pattern))

        if not heap:
            return []
        
        return list(heapq.heappop(heap)[1])

        


        
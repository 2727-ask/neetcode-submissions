class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = defaultdict(list)

        distances = defaultdict(float)

        for i in range(1, n+1):
            adjList[i] = []
            distances[i] = float('inf')
 
        for source, dest, weight in times:
            adjList[source].append((dest, weight))

        distances[k] = 0
        heap = [(0, k)]

        while(heap):
            dist, pop = heapq.heappop(heap)
            for child, weight in adjList[pop]:
                new_dist = dist + weight
                if(distances[child] > new_dist):
                    distances[child] = new_dist
                    heapq.heappush(heap, (new_dist, child))

        ans = max(distances.values()) 
        return -1 if ans == float('inf') else ans



            

            
    

        
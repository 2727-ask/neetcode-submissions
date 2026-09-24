class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        dist = [float("inf")] * (n+1)
        s = k
        dist[s] = 0
        for source, target, weight in times:
            adjList[source].append((target, weight))
            if(target not in adjList):
                adjList[target] = []

        print(adjList)
        
        # adjList = {
        #     1: [(2,1), (4,4)],
        #     2: [(3,1)],
        #     3: [(4, 1)],
        #     4: []
        # }


        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, s))


        while heap:
            par_dist, parent = heapq.heappop(heap)
            print(par_dist, parent)
            for child, d in adjList[parent]:
                newDist = par_dist + d
                if(dist[child] > newDist):
                    dist[child] = newDist
                    heapq.heappush(heap, (newDist, child))

        
        if(max(dist[1:]) == float("inf")):
                return -1

        return max(dist[1:])




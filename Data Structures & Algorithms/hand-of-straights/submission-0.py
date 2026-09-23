class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if(len(hand) % groupSize):
            return False

        counter = Counter(hand)

        heap = list(counter.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if counter[i] <= 0:
                    return False

                counter[i] = counter[i] - 1
                if(counter[i] <= 0):
                    heapq.heappop(heap)

        if(heap):
            return False
        else:
            return True



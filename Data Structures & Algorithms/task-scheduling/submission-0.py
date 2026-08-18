from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies of tasks
        freq = Counter(tasks)

        # 2. Build a Max Heap (using negative numbers since Python has a Min Heap)
        # We only need the counts, not the task names
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        queue = deque() # Stores pairs of: (remaining_count, available_time)
        clock = 0

        while maxHeap or queue:
            clock += 1

            # 3. Process a task if available in the heap
            if maxHeap:
                # Pop the most frequent task. 
                # Add 1 because the number is negative (e.g., -3 + 1 = -2)
                cnt = heapq.heappop(maxHeap) + 1 
                
                # If the task still has remaining executions, put it in cooldown
                if cnt != 0:
                    queue.append((cnt, clock + n))
            
            # 4. Check if the task at the front of the queue is ready
            if queue and queue[0][1] == clock:
                # Pop the ready task and push its remaining count back into the heap
                ready_task_count, _ = queue.popleft()
                heapq.heappush(maxHeap, ready_task_count)
                
        return clock
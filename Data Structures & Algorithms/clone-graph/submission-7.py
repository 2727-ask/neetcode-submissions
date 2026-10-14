"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return 
    
        queue = deque([])

        old_to_new = defaultdict()

        queue.append(node)

        while(queue):
            pop = queue.popleft()
            if(pop not in old_to_new):
                old_to_new[pop] = Node(pop.val)
                for child in pop.neighbors:
                    queue.append(child)

        for key, val in old_to_new.items():
            for child in key.neighbors:
                old_to_new[key].neighbors.append(old_to_new[child])

        return old_to_new[node]
            
            
          




        
        
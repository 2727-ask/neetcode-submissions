"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head is None):
            return None
        store = {}
        dummy = head
        while (dummy):
            node = Node(dummy.val, dummy.next, dummy.random)
            store[dummy] = node
            dummy = dummy.next
        
        for key, val in store.items():
            val.next = store.get(key.next)
            val.random = store.get(key.random)


        first_key = list(store.keys())[0]
        first_val = store[first_key]
                
        return first_val

         
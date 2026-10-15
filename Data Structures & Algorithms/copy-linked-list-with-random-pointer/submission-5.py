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
        if not head:
            return
        _map = {}

        dummy = head
        while(dummy):
            copy = Node(dummy.val)
            _map[dummy] = copy
            dummy = dummy.next

        for org, copy in _map.items():
            if(org.random):
                copy.random = _map[org.random]
            if(org.next):
                copy.next = _map[org.next]

        
        return _map[head]


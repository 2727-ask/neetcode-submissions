# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heap = []

        dummy = head
        new = ListNode(0)
        curr = new

        head_of_remainder = head
        
        i = 0
        while(dummy):
            if i == 0:
                head_of_remainder = dummy
            next_node = dummy.next
            i = i + 1
            heapq.heappush(heap, (-i, dummy))

            if(len(heap) == k):
                i = 0
                while(heap):
                    node = heapq.heappop(heap)[1]
                    curr.next = node 
                    curr = node
                curr.next = next_node

            dummy = next_node
        
        if heap:
            curr.next = head_of_remainder
        

        return new.next
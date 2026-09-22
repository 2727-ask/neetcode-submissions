# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        
        heap = []
        heapq.heapify(heap)

        for ll in lists:
            while(ll):
                heapq.heappush(heap, ll.val)
                ll = ll.next

        head = ListNode()
        dummy = head

        while heap:
            pop = heapq.heappop(heap)
            head.next = ListNode(pop)
            head = head.next
        
        return dummy.next

        
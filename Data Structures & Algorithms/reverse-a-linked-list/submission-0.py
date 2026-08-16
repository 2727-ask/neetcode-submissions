# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


        # [0,1,2,3]

        # processed = 0 -> None
        # unprocessed = 1 -> 2 -> 3

        # processed = 1 -> 0 - > None
        # unprocessed = 2 -> 3

        # processed = 2 -> 1 -> 0 -> None
        # unprocessed = 3

        # processed = 3 -> 2 -> 1 -> 0

        curr = head
        processed = None
        while(curr is not None):
            unprocessed = curr.next
            curr.next = processed

            processed = curr
            curr = unprocessed
        return processed



        
        


        




        
            

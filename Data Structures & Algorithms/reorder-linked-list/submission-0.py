# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #mid point identification

        slow = head
        fast = head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        print(slow.val)


        #reverse the second part

        processed = None
        curr = slow.next
        slow.next = None


        while(curr):
            unprocessed = curr.next
            curr.next = processed

            processed = curr
            curr = unprocessed
        
        part1 = head #[2,4,6]
        part2 = processed #[10,8]   


        while(part2):
            temp1 = part1.next
            temp2 = part2.next

            part1.next = part2
            part2.next = temp1

            part1 = temp1
            part2 = temp2


        
        

        # print(arr1)
        # print(arr2)


        
            

            


        
            






            



            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the min

        slow = head
        fast = head

        while(fast and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        processed = None
        while(mid):
            unprocessed = mid.next
            mid.next = processed

            processed = mid
            mid = unprocessed

        part1 = head
        part2 = processed


        while(part2):
            temp1 = part1.next
            temp2 = part2.next

            part1.next = part2
            part2.next = temp1

            part1 = temp1
            part2 = temp2






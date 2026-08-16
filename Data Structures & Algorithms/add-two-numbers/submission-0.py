# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        ans = []

        carry = 0

        def getCarry(no):
            if 10 <= abs(no) <= 99:
                tens = no // 10
                ones = no % 10
                return (ones, tens)
            else:
                return (no, 0)


        while(l1 and l2):
            curr = sum([l1.val, l2.val, carry])
            carry = 0
            no, carry = getCarry(curr)
            ans.append(no)
            l1 = l1.next
            l2 = l2.next
        
        
        while(l1):
            curr = sum([l1.val, carry])
            carry = 0
            no, carry = getCarry(curr)
            ans.append(no)
            l1 = l1.next
        
        while(l2):
            curr = sum([l2.val, carry])
            carry = 0
            no, carry = getCarry(curr)
            ans.append(no)
            l2 = l2.next


        if(carry != 0):
            ans.append(carry)

        head = ListNode(ans[0])
        dummy = head
        for x in ans:
            node = ListNode(x)
            dummy.next = node
            dummy = dummy.next

        

        print(ans)

        return head.next



        
        
                

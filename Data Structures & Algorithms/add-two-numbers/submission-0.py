# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ptr1 = l1
        ptr2 = l2
        digit, carry = 0,0
        prev = ListNode()
        head = prev

        while ptr1 or ptr2 or carry > 0:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0 

            sum = val1 + val2 + carry
            digit = int(sum%10)
            prev.next = ListNode(digit)
            carry = int(sum/10)
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            prev = prev.next

        return head.next


            





        
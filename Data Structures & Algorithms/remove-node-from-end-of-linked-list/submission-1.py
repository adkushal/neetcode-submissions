# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            return None
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        # n = size of list, we remove first element
        if not fast:
            head = head.next
            return head


        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete the node after slow
        temp = slow.next
        slow.next = temp.next
        temp = None

        return head
        
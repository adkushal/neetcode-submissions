# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        # Find one before middle of linked list
        # Needed because if we just find the middle, 
        #and reverse, the middle element will point to end of second list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two lists
        curr = slow.next
        slow.next = None
        prev = None
        # Reverse the second half of the linked list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Merge the two halfs to generate the pattern
        low = head
        high = prev

        while low.next:
            temp1 = low.next
            temp2 = high.next

            low.next = high
            high.next = temp1
            
            low = temp1
            high = temp2

        # If odd add the last element of right list to the left
        low.next = high




        
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
            return head
        seen = {}
        def getCopy(node):
            if not node:
                return None
            
            if node not in seen:
                seen[node] = Node(node.val)
            return seen[node]

        curr = head
        while curr:
            copy = getCopy(curr)
            copy.next = getCopy(curr.next)
            copy.random = getCopy(curr.random)
            curr = curr.next

        return seen[head]

            
        
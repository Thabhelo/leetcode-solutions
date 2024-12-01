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
        if not head: return None
        
        # Step 1: Create interleaved copies
        dummy = head
        while dummy:
            copy = Node(dummy.val, dummy.next, dummy.random)
            dummy.next = copy
            dummy = copy.next

        # Step 2: Separate the original and copied lists
        dummy, copy_head = head.next, head.next
        while dummy:
            if dummy.next:
                dummy.next = dummy.next.next
            if dummy.random:
                dummy.random = dummy.random.next
            dummy = dummy.next
        return copy_head
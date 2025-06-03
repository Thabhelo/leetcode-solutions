# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Queue to temporarily store the big nodes
        big_nodes_queue = deque()
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        # First pass: remove big nodes and load them in our queue, keep small nodes in place
        while curr:
            if curr.val >= x:
                # Remove this guy from current position and queue him
                big_nodes_queue.append(curr)
                prev.next = curr.next  # Skip this node
                curr = curr.next
            else:
                # Keep small node in place, just move forward
                prev = curr
                curr = curr.next
        
        # Now prev points to the last small node
        # Append all the queued big nodes at the end
        while big_nodes_queue:
            node = big_nodes_queue.popleft()
            prev.next = node
            prev = node
        
        # Terminate the list properly
        prev.next = None
        
        return dummy.next

        
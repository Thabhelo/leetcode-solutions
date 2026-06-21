# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # 1. reverse the second half
        # 2. now merge them

        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second_head starts at the beginning of the second half
        second_head = slow.next
        slow.next = None  # Split the list into two halves
        # reverse the second linked list
        prev = None
        curr = second_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_head = prev

        # 2. interleave/Merge the two halves unconditionally
        first_head = head
        while second_head:
            # Save next nodes
            tmp1 = first_head.next
            tmp2 = second_head.next
            
            # Interleave pointers
            first_head.next = second_head
            second_head.next = tmp1
            
            # Move pointers forward
            first_head = tmp1
            second_head = tmp2
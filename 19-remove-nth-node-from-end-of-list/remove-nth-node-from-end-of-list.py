# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head

        for _ in range(n):
            right = right.next

        # If right is None, it means n is equal to the length of the list.
        # The node to remove is the head itself.
        if not right:
            return head.next

        guy_n_steps_behind = left
        guy_n_steps_ahead = right

        while guy_n_steps_ahead and guy_n_steps_ahead.next:
            guy_n_steps_behind = guy_n_steps_behind.next
            guy_n_steps_ahead = guy_n_steps_ahead.next

        # at this point, the two pointers that are n steps apart, have reached the end (the rightmost one has reached the end)
        # and the ListNode we wanna delete (basically skip) is the one just one step after the leftmost pointer. (guy_n_steps_behind.next)

        to_be_skipped = guy_n_steps_behind.next
        new_next = to_be_skipped.next

        guy_n_steps_behind.next = new_next

        return head





        


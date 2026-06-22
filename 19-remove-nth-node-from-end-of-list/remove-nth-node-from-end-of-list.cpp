/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Create a dummy node that points to head.
        // This will help us avoid special cases when deleting the head itself.
        ListNode dummy(0);
        dummy.next = head;

        // Both pointers start at dummy
        ListNode* left = &dummy;
        ListNode* right = &dummy;

        // Then we move the right pointer n+1 steps ahead
        // To create a gap of exactly n nodes between left and right
        for (int i = 0; i <= n; i++) {
            right = right->next;
        }

        // Then we move pointers together now until right reaches the end
        // Since the gaps here will now stay constnat, left will end up 
        // immediately BEFORE the node we want to remove (technically skip))
        while (right) {
            left = left->next;
            right = right->next;
        }
        
        // this would have skipped over the target node

        left->next = left->next->next; // skip

        return dummy.next;
    }
};
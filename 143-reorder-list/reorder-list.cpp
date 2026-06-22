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
    void reorderList(ListNode* head) {
        // edge case
        if (!head || !head->next) {
            return;
        }
        
        // 1. find middle
        // 2. split list
        // 3. reverse second half
        // merge first half + reversed second half

        //find middle
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        // slow is now just around the middle, second half starts just after
        ListNode* second_head = slow->next;

        // break the list into two distinct lists
        slow->next = nullptr;

        // 2. reverse second half
        ListNode* prev = nullptr;
        ListNode* curr = second_head;
        while (curr) {
            ListNode* nxt = curr->next; // save a copy of second_head.next
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }

        // prev is now the head of the reversed second half
        second_head = prev;

        // 3. merge
        ListNode* first_head = head;
        while (second_head) {
            //Save next nodes into temporary variables before changing pointers
            ListNode* tmp1 = first_head->next;
            ListNode* tmp2 = second_head->next;

            // put one node from second half after one node from first half
            first_head->next = second_head;
            second_head->next = tmp1;

            // move both pointers
            first_head = tmp1;
            second_head = tmp2;
        }

    }
};
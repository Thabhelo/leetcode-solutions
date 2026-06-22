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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // we might need a dmmy that will poit to the new head of the result
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0; // simply to carry the remainders

        while (l1 || l2 || carry) {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;

            int total = val1 + val2 + carry;

            carry = total / 10;

            // create the new node and advance the ponter
            curr->next = new ListNode(total % 10);
            curr = curr->next;

            if (l1) {
                l1 = l1->next;
            }

            if (l2) {
                l2 = l2->next;
            }
        } 
        return dummy->next;

    }
};
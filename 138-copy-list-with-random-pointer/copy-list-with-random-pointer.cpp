/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return nullptr;
        }

        // 1. lets map the original to the new copy, node by node
        // 2. and then create thenodes without any pointers in the first pass
        // 3. then reset curr variable back to head and do a second pass and assign pointers

        // 1. maps orignal nodes to their clones
        unordered_map<Node*, Node*> old_to_new;
        old_to_new[nullptr] = nullptr;

        // first pass, create all new nodes
        Node* curr = head;

        while (curr) {
            old_to_new[curr] = new Node(curr->val);
            curr = curr->next;
        }
        // seocnd pass, connect the next and random pointers
        curr = head;
        
        while (curr) {
            Node* new_node = old_to_new[curr];

            new_node->next = old_to_new[curr->next];
            new_node->random = old_to_new[curr->random];

            curr = curr->next;
        }
        return old_to_new[head];
        
    }
};
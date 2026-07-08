/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        // Explicitly define the type so it can reference itself
        std::function<void(TreeNode*, vector<int>&)> getLeaves = [&](TreeNode* root, vector<int>& leaves) {
            if (!root) return;
            if (!root->left && !root->right) {
                leaves.push_back(root->val); // Note: use root->val, not root.val
                return;
            }
            getLeaves(root->left, leaves);
            getLeaves(root->right, leaves);
        };

        vector<int> leaves1, leaves2;
        getLeaves(root1, leaves1);
        getLeaves(root2, leaves2);
        
        return leaves1 == leaves2;
    };
};
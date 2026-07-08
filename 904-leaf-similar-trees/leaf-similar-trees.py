# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_values(node):
            if not node: return []
            if not node.left and not node.right: # It's a leaf node
                return [node.val]
            # recursively get leaves from left and right subtrees
            return get_leaf_values(node.left) + get_leaf_values(node.right)

        # get leaf sequences for both trees
        return get_leaf_values(root1) == get_leaf_values(root2)


        
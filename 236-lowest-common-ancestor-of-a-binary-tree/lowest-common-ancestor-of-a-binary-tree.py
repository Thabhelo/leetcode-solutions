# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_helper(node):
            if not node:
                return None  # \U0001f3a8 Base case: null node found nothing
            
            # \U0001f3a8 Special case: Current node is one of our targets!
            if node == p or node == q:
                return node
            
            left_result = dfs_helper(node.left)
            right_result = dfs_helper(node.right)
            
            # \U0001f3a8 Combine: If both children found something, we're the LCA!
            if left_result and right_result:
                return node
            
            # \U0001f3a8 Otherwise, bubble up whatever we found
            return left_result or right_result
        
        return dfs_helper(root)
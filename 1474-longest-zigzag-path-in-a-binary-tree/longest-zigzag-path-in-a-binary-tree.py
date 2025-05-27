
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        DFS approach tracking direction and length at each node.
        Returns the maximum zigzag length found.
        """
        if not root:
            return 0
        
        max_length = 0
        
        def dfs(node, direction, length):
            if not node:
                return
            
            # Update global maximum
            nonlocal max_length
            max_length = max(max_length, length)
            
            if direction == 'left':
                # If we came from left, next must go right for zigzag
                # Or we can start fresh from left
                dfs(node.right, 'right', length + 1)
                dfs(node.left, 'left', 1)
            else:  # direction == 'right'
                # If we came from right, next must go left for zigzag
                # Or we can start fresh from right
                dfs(node.left, 'left', length + 1)
                dfs(node.right, 'right', 1)
        
        # Start from both directions
        dfs(root.left, 'left', 1)
        dfs(root.right, 'right', 1)
        
        return max_length
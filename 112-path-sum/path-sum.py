# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: an empty node/tree has no paths
        if not root:
            return False
        
        # If it's a leaf node, check if the remaining sum equals the node's value
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Decrement targetSum by the current node's value for the subtrees
        remaining_sum = targetSum - root.val
        
        # Return True if either the left path or right path finds the target sum
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum)
        

        
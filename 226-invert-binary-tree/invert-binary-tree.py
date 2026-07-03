# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Null check
        if not root:
            # 2. Return None if empty
            return None
        
        # Initialize a stack with the root node
        stack = [root]
        
        while stack:
            # Pop the most recently added node (LIFO)
            current = stack.pop()
            
            # Swap the current node's children
            current.left, current.right = current.right, current.left
            
            # Push valid children onto the stack to process next
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
                
        return root
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
        
        # Initialize a queue with the root node
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            
            # Swap the current node's children
            current.left, current.right = current.right, current.left
            
            # Add valid children to the queue to be processed later
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
        return root
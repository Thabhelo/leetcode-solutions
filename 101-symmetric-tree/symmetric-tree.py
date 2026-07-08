# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Helper function to compare two mirrored subtrees
        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            # 1. Check if current values match
            # 2. Compare t1's left subtree with t2's right subtree
            # 3. Compare t1's right subtree with t2's left subtree
            return (t1.val == t2.val) and \
                   is_mirror(t1.left, t2.right) and \
                   is_mirror(t1.right, t2.left)
        
        return is_mirror(root.left, root.right)
        
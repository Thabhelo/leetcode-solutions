# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both trees are empty
        if not p and not q:
            return True

        # Base case: one tree is empty while the other isn't, or values don't match
        if not p or not q or p.val != q.val:
            return False

        # Recursive step: compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
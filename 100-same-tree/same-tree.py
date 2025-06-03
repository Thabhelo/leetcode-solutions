# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, they are identical
        if not p and not q: 
            return True
        # If only one is None, they are not identical
        if not p or not q: 
            return False

        stack = [(p, q)]  # Initialize stack with root nodes

        while stack:
            node_p, node_q = stack.pop()  # Pop a pair of nodes

            # Compare values
            if node_p.val != node_q.val:
                return False

            # Push left children if they exist
            if node_p.left and node_q.left:
                stack.append((node_p.left, node_q.left))  # Push left children pair
            # If one left child is None and the other is not, not identical
            elif node_p.left or node_q.left: 
                return False

            # Push right children if they exist
            if node_p.right and node_q.right:
                stack.append((node_p.right, node_q.right))  # Push right children pair
            # If one right child is None and the other is not, not identical
            elif node_p.right or node_q.right: 
                return False

        # If the loop finishes, all nodes matched
        return True
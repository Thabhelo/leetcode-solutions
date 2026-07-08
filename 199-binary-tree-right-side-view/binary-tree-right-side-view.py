# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            
            # If this is the first time we've reached this depth, 
            # it must be the rightmost node seen so far.
            if depth == len(result):
                result.append(node.val)
            
            # Prioritize right side exploration
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return result

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = {}

        def dfs(node: TreeNode, level: int) -> None:
            if not node:
                return 

            # add current node's value to its level sum
            level_sums[level] = level_sums.get(level, 0) + node.val
            # recurse for left and right children
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        # Find the smallest level with maximum sum
        max_sum = float('-inf')
        result_level = 1
        
        for level, sum_val in level_sums.items():
            if sum_val > max_sum:
                max_sum = sum_val
                result_level = level
                
        return result_level

        



        



        
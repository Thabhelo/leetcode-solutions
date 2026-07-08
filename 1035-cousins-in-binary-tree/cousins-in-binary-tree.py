# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return False
        
        # Queue stores pairs of (current_node, parent_node)
        queue = deque([(root, None)])

        while queue:
            level_size = len(queue)
            found_x = None  # Will store parent of x if found
            found_y = None  # Will store parent of y if found

            for _ in range(level_size):
                node, parent = queue.popleft()
                
                if node.val == x:
                    found_x = parent
                if node.val == y:
                    found_y = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # After checking the current level, evaluate if we found x and/or y
            if found_x and found_y:
                # True if they are on the same level but have different parents
                return found_x != found_y
            
            if found_x or found_y:
                return False

        return False




        
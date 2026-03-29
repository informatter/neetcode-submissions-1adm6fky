# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        queue = deque([root])
        levels.append([root.val])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
            if level:
                levels.append(level)

            
               
        return levels



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        queue = []
        queue.append(root)
        levels.append([root.val])
        i=0
        while queue:

            level = []
            for _ in range(len(levels[i])):
                node = queue.pop(0)

                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
            if level:
                levels.append(level)
            i+=1

            
               
        return levels



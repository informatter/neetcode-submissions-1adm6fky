# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS can be used for traversing as deep as possible donw a path.
        if not root:
            return 0
        l_h = self.maxDepth(root.left)
        r_h = self.maxDepth(root.right)
        # +1 is added so leaf nodes count by 1. 
        # max is needed so maximum depth from the current node's left and right subtrees is determined. 
        # Recursion naturally will buble up the answer to parent nodes.
        return 1+max(l_h,r_h)


        
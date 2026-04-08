# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self._max = 0
    def _dfs(self, node:TreeNode) -> int:
        if not node:
            return 0
        
        l_height = self._dfs(node.left)
        r_height = self._dfs(node.right)
        self._max = max(self._max,r_height+l_height)
        # nodes without children will always have a height of 1 [1+max(0,0)]
        return 1 + max(r_height,l_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS can be used by traversing left sub tree then right subtree (order does not matter) and 
        # keep track of the height of each node from its local perspective (subtree). When nodes are popped, height
        # increments and `self._max` is updated.
        self._dfs(root)
        return self._max
        
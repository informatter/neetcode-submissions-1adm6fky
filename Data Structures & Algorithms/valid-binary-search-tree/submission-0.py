# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # This problem needs us to pass info top down so we can compare current node.val against parent.val
        # We also need to make sure that the current node's value is within the range of the root and parents value.


        def _dfs(node:TreeNode|None,root_val:int, parent_val:int ):

            if not node:
                return True

            if node.val <= root_val or node.val >= parent_val:
                return False
            
            # the left subtree will always use the root's original value (-inf) while updating the parents value.
            # the right subtree will always use the parents value as the root value and keep the parents value fixed (inf)
            lst =  _dfs(node.left,root_val, node.val )
            rst = _dfs(node.right,node.val,parent_val)
            return lst and rst


        return _dfs(root,-inf, inf)


        
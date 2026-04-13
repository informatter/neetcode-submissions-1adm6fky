# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def _is_same(p:None|TreeNode,q:None|TreeNode): 
            if p is None and q is None: 
                return True 
            if p is None or q is None: 
                return False 
            if p.val != q.val: 
                return False 
            return _is_same(p.left,q.left)  and _is_same(p.right,q.right)

        def traverse(root:None|TreeNode, subRoot:None|TreeNode):
            if not subRoot:
                return True
            if not root:
                return False

            if _is_same(root,subRoot):
                return True


            # search -> keep subRoot fixed
            return traverse(root.left,subRoot) or traverse(root.right,subRoot)

        
        return traverse(root,subRoot)
        
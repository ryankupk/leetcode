// https://leetcode.com/problems/evaluate-boolean-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if root is None:
                return
            if root.val == 0:
                return False
            if root.val == 1:
                return True
            l = traverse(root.left)
            r = traverse(root.right)
            if root.val == 2:
                return l or r
            elif root.val == 3:
                return l and r
            
        
        fin = traverse(root)
        return fin
        # return eval(' '.join(statement))
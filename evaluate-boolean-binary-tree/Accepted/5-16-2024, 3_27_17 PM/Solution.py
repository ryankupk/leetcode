// https://leetcode.com/problems/evaluate-boolean-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)
        
        if root.val == 2:
            return left_result or right_result
        elif root.val == 3:
            return left_result and right_result
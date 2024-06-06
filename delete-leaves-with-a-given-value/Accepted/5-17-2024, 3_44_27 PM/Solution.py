# https://leetcode.com/problems/delete-leaves-with-a-given-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def traverse(root):
            if root is None:
                return None
            
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            if root.left is None and root.right is None and root.val == target:
                return None
            return root

        return traverse(root)
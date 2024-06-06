// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root.val == val:
            return root
        def traverse(root):
            if root is None:
                return None
            
            left = traverse(root.left)
            right = traverse(root.right)
            if left is not None and left.val == val:
                return left
            if right is not None and right.val == val:
                return right
            return root
            
        sub = traverse(root)
        if sub == root:
            return None
        return sub
        
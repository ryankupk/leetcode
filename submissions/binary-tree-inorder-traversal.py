# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def traverse(root, nodes):
            if root is None:
                return 
            
            traverse(root.left, nodes)
            nodes.append(root.val)
            traverse(root.right, nodes)

        traverse(root, nodes)
        return nodes
# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def inorder(root, path):

            if root is None:
                return
            
            left = inorder(root.left, path)
            right = inorder(root.right, path)

            path.append(left)
            path.append(right)
            path.append(root.val)
            return root.val

            
        p_path = []
        q_path = []

        inorder(p, p_path)
        inorder(q, q_path)

        print(f"{p_path=}")
        print(f"{q_path=}")
        return p_path == q_path
            
        
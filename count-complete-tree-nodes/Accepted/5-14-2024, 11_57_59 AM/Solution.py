# https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse_tree(self, root, nodes): 
        # print(f"{nodes=}")
        if root.left is None and root.right is None:
            nodes.append(root.val)
        else:
            nodes.append(root.val)
            if root.left is not None:
                self.traverse_tree(root.left, nodes)
            if root.right is not None:
                self.traverse_tree(root.right, nodes)


    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        nodes = []
        self.traverse_tree(root, nodes)
        return len(nodes)
# https://leetcode.com/problems/distribute-coins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.num_moves = 0

        def traverse(node):
            if node is None:
                return 0

            left_excess = traverse(node.left)
            right_excess = traverse(node.right)

            self.num_moves += abs(left_excess) + abs(right_excess)

            return node.val + left_excess + right_excess - 1

        traverse(root)
        return self.num_moves

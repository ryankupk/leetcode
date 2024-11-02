/*
 * @lc app=leetcode id=111 lang=golang
 *
 * [111] Minimum Depth of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	left := minDepth(root.Left)
	right := minDepth(root.Right)

	if left == 0 && right != 0 {
		return 1 + right
	} else if left != 0 && right == 0 {
		return 1 + left
	} else if left == 0 && right == 0 {
		return 1
	} else if right != 0 && left != 0 {
		return 1 + min(left, right)
	}

	return 1 + min(left, right)
}

// @lc code=end


/*
 * @lc app=leetcode id=110 lang=golang
 *
 * [110] Balanced Binary Tree
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
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func traverse(root *TreeNode) int { // right track as per perplexity
	if root == nil {
		return 0
	}

	leftHeight := traverse(root.Left)
	if leftHeight == -1 {
		return -1
	}
	rightHeight := traverse(root.Right)
	if rightHeight == -1 {
		return -1
	}

	if abs(leftHeight-rightHeight) > 1 {
		return -1
	}

	return 1 + max(leftHeight, rightHeight)
}
func isBalanced(root *TreeNode) bool {
	return traverse(root) != -1
}

// @lc code=end


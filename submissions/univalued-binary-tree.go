/*
 * @lc app=leetcode id=965 lang=golang
 *
 * [965] Univalued Binary Tree
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
func isUnivalTree(root *TreeNode) bool {
    
	if root == nil {
		return true
	}

	ret := true
	left := isUnivalTree(root.Left)
	right := isUnivalTree(root.Right)

	if root.Left != nil && root.Left.Val != root.Val {
		ret = false
	}
	if root.Right != nil && root.Right.Val != root.Val {
		ret = false
	}

	return ret && left && right
}

// @lc code=end


// https://leetcode.com/problems/maximum-depth-of-binary-tree

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import (
	"fmt"
)

func dfs(root *TreeNode) int {

	if root.Left == nil && root.Right == nil {
		return 1
	}

	left, right := 0, 0
	if root.Left != nil {
		left = dfs(root.Left)
	}
	if root.Right != nil {
		right = dfs(root.Right)
	}

	maxSubTree := max(left, right)
	return 1 + maxSubTree

}
func maxDepth(root *TreeNode) int {
	fmt.Println(root)
	if root == nil {
		return 0
	}
	maxDepthCount := dfs(root)
	return maxDepthCount

}

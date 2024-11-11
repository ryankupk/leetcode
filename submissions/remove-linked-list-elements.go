/*
 * @lc app=leetcode id=203 lang=golang
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	res := head

	for head != nil {
		for head.Next != nil && head.Next.Val == val {
			head.Next = head.Next.Next
		}
		head = head.Next
	}

	if res != nil && res.Val == val {
		return res.Next
	}

	return res
}

// @lc code=end


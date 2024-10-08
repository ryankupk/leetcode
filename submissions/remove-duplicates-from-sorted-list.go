/*
 * @lc app=leetcode id=83 lang=golang
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	saveHead := head

	for head != nil && head.Next != nil {
		for head.Next != nil && head.Next.Val == head.Val {
			head.Next = head.Next.Next
		}
		head = head.Next
	}

	return saveHead
}

// @lc code=end


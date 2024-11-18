/*
 * @lc app=leetcode id=82 lang=golang
 *
 * [82] Remove Duplicates from Sorted List II
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
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return head
	}
	if head.Next != nil && head.Next.Val == head.Val && head.Next.Next == nil {
		return nil
	}

	for head != nil && head.Next != nil && head.Val == head.Next.Val {
		duplicateValue := head.Val
		for head != nil && head.Next != nil && head.Val == duplicateValue {
			head = head.Next
		}
		if head.Val == duplicateValue {
			head = head.Next
		}
	}
	if head == nil {
		return nil
	} // end of edge case hell

	save := head

	for head != nil {
		if head.Next != nil && head.Next.Next != nil && head.Next.Val == head.Next.Next.Val {
			duplicateValue := head.Next.Val
			head.Next = head.Next.Next.Next
			for head.Next != nil && head.Next.Val == duplicateValue {
				head.Next = head.Next.Next
			}
		} else {
			head = head.Next
		}
	}

	return save
}

// @lc code=end

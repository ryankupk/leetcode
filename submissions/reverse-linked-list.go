/*
 * @lc app=leetcode id=206 lang=golang
 *
 * [206] Reverse Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	newHead := &ListNode{Val: 0, Next: nil} // line 13
	saveNewHead := newHead

	nodeVals := make([]int, 0)

	for head != nil {
		nodeVals = append(nodeVals, head.Val)
		head = head.Next
	}

	for i := len(nodeVals) - 1; i >= 1; i-- {
		newHead.Val = nodeVals[i]
		newNode := &ListNode{Val: 0, Next: nil} // line 24
		newHead.Next = newNode
		newHead = newHead.Next
	}
	newHead.Val = nodeVals[0]

	return saveNewHead

}

// @lc code=end


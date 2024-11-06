/*
 * @lc app=leetcode id=23 lang=golang
 *
 * [23] Merge k Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
	nonEmptyLists := make([]*ListNode, 0)
	for _, list := range lists {
		if list != nil {
			nonEmptyLists = append(nonEmptyLists, list)
		}
	}

	if len(nonEmptyLists) == 0 {
		return nil
	}

	dummy := &ListNode{0, nil}
	current := dummy

	for len(nonEmptyLists) > 0 {
		smallestIdx := 0
		smallestVal := math.MaxInt32

		for i, list := range nonEmptyLists {
			if list.Val < smallestVal {
				smallestVal = list.Val
				smallestIdx = i
			}
		}

		current.Next = nonEmptyLists[smallestIdx]
		current = current.Next
		nonEmptyLists[smallestIdx] = nonEmptyLists[smallestIdx].Next

		if nonEmptyLists[smallestIdx] == nil {
			nonEmptyLists = append(nonEmptyLists[:smallestIdx], nonEmptyLists[smallestIdx+1:]...)
		}
	}

	return dummy.Next
}

// @lc code=end


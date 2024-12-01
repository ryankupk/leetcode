/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    if head.Next == nil {
        return head
    }

    slow, fast := head.Next, head.Next.Next    

    for fast != nil {
        if fast.Next != nil {
            fast = fast.Next.Next
        } else {
            fast = nil
            break
        }
        slow = slow.Next
    }

    return slow
}

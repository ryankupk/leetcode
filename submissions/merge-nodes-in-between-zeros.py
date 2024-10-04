# https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        prev, curr = dummy, head.next

        while curr:
            sum = 0
            while curr.val != 0:
                sum += curr.val
                curr = curr.next
            prev.next = ListNode(sum)
            prev = prev.next
            curr = curr.next

        return dummy.next
        
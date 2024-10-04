# https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        return_head = head

        while head is not None and head.next is not None:
            temp = head.next.val
            head.next.val = head.val
            head.val = temp
            head = head.next.next

        return return_head
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        save_head = head

        while head is not None and head.next is not None:
            node_gcd = gcd(head.val, head.next.val)
            save_next = head.next
            head.next = ListNode(node_gcd, save_next)
            head = head.next.next

        return save_head
        
        
# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def join_list(self, l1: Optional[ListNode]) -> int:
        num_str = ''
        while l1 != None:
            num_str += str(l1.val)
            l1 = l1.next
        return int(num_str[::-1])

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added_nums = str(self.join_list(l1) + self.join_list(l2))[::-1]
        if len(added_nums) == 0: return ListNode()
        elif len(added_nums) == 1: return ListNode(int(added_nums))
        
        head = ListNode(val=added_nums[0])
        next_node = ListNode(val=added_nums[1])
        head.next = next_node
        if len(added_nums) == 2: return head
        
        for digit in added_nums[2:]:
            next_node.next = ListNode(val=digit)
            next_node = next_node.next
        return head
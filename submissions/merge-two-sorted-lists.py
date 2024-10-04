# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import copy
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return 

        new_list = ListNode()
        new_list_head = new_list

        while (list1 is not None or list2 is not None):
            if list1 is None:
                while list2 is not None:
                    new_list.next = ListNode(list2.val)
                    new_list = new_list.next
                    list2 = list2.next
                break
            if list2 is None:
                while list1 is not None:
                    new_list.next = ListNode(list1.val)
                    new_list = new_list.next
                    list1 = list1.next
                break
            if list1.val <= list2.val:
                new_list.next = ListNode(list1.val)
                new_list = new_list.next
                list1 = list1.next
            else:
                new_list.next = ListNode(list2.val)
                new_list = new_list.next
                list2 = list2.next

        return new_list_head.next
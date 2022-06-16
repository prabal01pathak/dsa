#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        head_first = list1
        head_second = list2
        new_head = None
        i = 0
        pointer = None
        while head_first and head_second:
            if not i:
                if head_first.val > head_second.val:
                    new_head = head_second
                    pointer = new_head
                    head_second = head_second.next
                else:
                    new_head = head_first
                    pointer = new_head
                    head_first = head_first.next
            elif head_first.val > head_second.val:
                pointer.next = head_second
                pointer = pointer.next
                head_second = head_second.next
            else:
                pointer.next = head_first
                pointer = pointer.next
                head_first = head_first.next
            i += 1
        if head_first:
            pointer.next = head_first
        elif head_second:
            pointer.next = head_second
        return new_head


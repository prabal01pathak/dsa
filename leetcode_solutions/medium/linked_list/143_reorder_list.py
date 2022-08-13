#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        reverse_head, slow.next = slow.next, None
        # reverse nodes
        cur = reverse_head
        prev = None
        while cur:
            temp, cur = cur, cur.next
            temp.next, prev = prev, temp
        reverse_head, slow = prev, head
        fast = reverse_head
        while fast:
            temp, slow = slow, slow.next
            temp2, fast = fast, fast.next
            temp.next, temp2.next = temp2, slow

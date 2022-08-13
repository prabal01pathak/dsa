#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        for _ in range(n):
            fast_ptr = fast_ptr.next
            
        if not fast_ptr:
            return head.next

        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head

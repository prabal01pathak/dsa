#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.prev = None
        self.big_node = None

    def partition(self, head: Optional[ListNode], x: int) -> ListNode:
        if not root:
            return None
        dummy = ListNode(0, head)
        prev, cur = dummy, dummy.next
        # rearrange the values based on condition
        dummy = self.rearrange(self, dummy, x)
        return dummy

    def set_value(self, temp):
        temp.next = self.big_node
        self.prev.next = temp
        self.prev = temp


    def rearrange(self, dummy, x):
        prev, cur = dummy, dummy.next
        while cur and cur < x:
            prev, cur = cur, cur.next
        self.prev = prev
        self.big_node = cur
        while cur:
            if cur and cur.val < x:
                temp = cur
                prev.next, cur = cur.next, cur.next 
                self.set_value(temp)
            else:
                prev, cur = cur, cur.next
        return dummy


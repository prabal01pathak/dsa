#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        prev = None
        while cur:
            if cur.val == val:
                if not prev:
                    temp = cur 
                    head = cur.next
                    temp.next = None
                    cur = head
                else:
                    temp = cur
                    prev.next = cur.next
                    temp.next = None
                    cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head

# recursive solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next


def test_removeElements():
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    val = 6
    head = s.removeElements(head, val)
    assert head.val == 1


if __name__ == '__main__':
    test_removeElements()
    print("================================== Test passed ==================================")

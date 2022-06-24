#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_head = head
        even_head = head.next
        e1 = even_head
        while odd_head and even_head:
            if odd_head.next:
                odd_head.next = odd_head.next.next
                odd_head = odd_head.next
            if even_head.next:
                even_head.next = even_head.next.next
                even_head = even_head.next
        current = head
        while current.next:
            current = current.next
        current.next = e1
        return head


def test_oddEvenList():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(6)
    h = Solution().oddEvenList(head)
    while h:
        h = h.next
        if h:
            print(h.val, end=" -> ")


if __name__ == "__main__":
    test_oddEvenList()

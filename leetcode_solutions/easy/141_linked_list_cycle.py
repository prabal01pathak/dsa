#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


def test_hasCycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head
    assert Solution().hasCycle(head) == True


def test_hasCycle_no_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    assert Solution().hasCycle(head) == False


def test_hasCycle_empty_list():
    assert Solution().hasCycle(None) == False


def test_hasCycle_single_node():
    head = ListNode(1)
    assert Solution().hasCycle(head) == False


def test_hasCycle_single_node_cycle():
    head = ListNode(1)
    head.next = head
    assert Solution().hasCycle(head) == True


def test_hasCycle_two_node_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert Solution().hasCycle(head) == True


if __name__ == '__main__':
    test_hasCycle()
    test_hasCycle_no_cycle()
    test_hasCycle_empty_list()
    test_hasCycle_single_node()
    test_hasCycle_single_node_cycle()
    test_hasCycle_two_node_cycle()
    print('Tests Passed!')

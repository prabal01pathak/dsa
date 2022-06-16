#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        prev = None
        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        return prev


def test_solution():
    from utils import to_list
    from utils import to_linked_list

    solution = Solution()

    head = to_linked_list([1, 2, 3, 4, 5])
    assert to_list(solution.reverseList(head)) == [5, 4, 3, 2, 1]


if __name__ == '__main__':
    test_solution()
    print("============================ Test Passed ============================")

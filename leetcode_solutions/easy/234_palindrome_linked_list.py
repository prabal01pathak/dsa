#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow_ptr = head
        fast_ptr = head
        head2 = None
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            temp = slow_ptr
            slow_ptr = slow_ptr.next
            temp.next= head2
            head2 = temp
        if fast_ptr:
            slow_ptr = slow_ptr.next
        while head2:
            if head2.val != slow_ptr.val:
                return False
            head2 = head2.next
            slow_ptr = slow_ptr.next
        return True


def test_isPalindrome():
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(1)
    h = Solution().isPalindrome(head)
    print(h)


if __name__ == "__main__":
    test_isPalindrome()

# 1 2 3 4 5

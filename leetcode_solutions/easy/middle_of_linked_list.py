#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional
from math import ceil

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        first = 0
        last = self.__len__(head)
        last = ceil(last//2) if last % 2 != 0 else last//2+1
        current = head
        while current:
            if first == last:
                break
            first += 1
            current = current.next
        return current

        
    def __len__(self, current):
        last = 0
        while current:
            current = current.next
            last += 1
        return last

    def repr(self,ll):
        while ll:
            print(ll.val)
            ll = ll.next

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next.next = ListNode(10)
    solution = Solution()
    print(solution.repr(solution.middleNode(head)))

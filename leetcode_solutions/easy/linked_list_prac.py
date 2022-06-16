#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, x):
        node = ListNode(x)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def print_list(self):
        cur = self.head
        items = []
        print(items)
        while cur:
            items.append(cur.val)
            cur = cur.next
        return "->".join(map(str, items))

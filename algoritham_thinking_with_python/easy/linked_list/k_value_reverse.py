#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linked_list import LinkedList, Node


def reverse_k_blocks(head: Node, k: int) -> Node:
    if not head or not head.next:
        return head
    current = head.next
    prev = head
    prev.next = None
    count = 0
    while current:
        if count != k - 3:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
            count += 1
        else:
            count = 0
    head = prev
    return head


def test_reverse_k_blocks():
    ll = LinkedList()
    l = [3,2,1]
    ll.create_from_list(l)
    print(ll.print_list())
    h = reverse_k_blocks(ll.head, 3)
    ll.head = h
    print(ll.print_list())


if __name__ == "__main__":
    test_reverse_k_blocks()


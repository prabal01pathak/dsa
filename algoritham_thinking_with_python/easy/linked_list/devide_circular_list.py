#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linked_list import LinkedList, Node
from floyd_cycle import make_cycle


def devide_circular_linked_list(head):
    if not head:
        return head
    slow_ptr = head
    fast_ptr = head
    while fast_ptr.next != head and fast_ptr.next.next != head:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    if fast_ptr.next == head:
        new_head = slow_ptr.next
        fast_ptr.next = None
        slow_ptr.next = None
        return head, new_head
    new_head = slow_ptr.next
    fast_ptr.next.next = None
    slow_ptr.next = None
    return head, new_head


def test_devide_circular_list():
    node = Node(5)
    ll = LinkedList(node)
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(8))
    ll.insert_at_end(Node(9))
    ll.insert_at_end(Node(9))
    ll.insert_at_end(Node(8))
    ll.insert_at_end(Node(8))
    ll.insert_at_end(Node(8))
    ll.insert_at_end(Node(8))
    print(ll.print_list())
    head = make_cycle(ll.head)
    first, second = devide_circular_linked_list(head)
    ll.head = first
    print(ll.print_list())
    ll.head = second
    print(ll.print_list())


if __name__ == "__main__":
    test_devide_circular_list()

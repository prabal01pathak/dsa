#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linked_list import LinkedList, Node
from floyd_cycle import make_cycle


def find_len_cycle(head):
    if not head:
        return False
    current = head
    slow_ptr = head
    fast_ptr = head
    length = 0
    while current.next and current.next.next:
        length += 1
        slow_ptr = slow_ptr.next
        fast_ptr = current.next.next
        if slow_ptr == fast_ptr:
            return length
            break
        current = current.next.next
    if not current.next or not current.next.next:
        return False
    slow_ptr = head
    while slow_ptr:
        if slow_ptr == fast_ptr:
            return slow_ptr
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next


def test_find_len_cycle():
    head = Node(5)
    ll = LinkedList(head)
    ll.insert_at_end(Node(6))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    ll.insert_at_end(Node(7))
    print(ll.print_list())
    head = make_cycle(ll.head)
    print(find_len_cycle(head))


if __name__ == "__main__":
    test_find_len_cycle()



#!/usr/bin/env python
# -*- coding: utf-8 -*-
from linked_list import Node, LinkedList


def floyd_cycle(head):
    if not head:
        return False
    slow_ptr = fast_ptr = head
    current = head
    while current.next:
        slow_ptr = current.next
        fast_ptr = current.next.next
        if slow_ptr == fast_ptr:
            return True
        current = current.next
    return False


def test_floyd_cycle():
    head = Node(2)
    ll = LinkedList()
    ll.insert_at_end(Node(3))
    ll.insert_at_end(Node(5))
    head = make_cycle(head)
    print(floyd_cycle(head))

def make_cycle(head):
    current = head
    first = head
    while current.next:
        current = current.next
    current.next = head
    return head



if __name__ == "__main__":
    test_floyd_cycle()


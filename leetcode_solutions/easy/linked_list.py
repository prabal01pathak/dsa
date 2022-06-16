#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def preppend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def pop(self, index=0):
        if not index:
            head = self.head
            self.head = self.head.next
            head.next = None
            return head.data
        else:
            current = self.head
            prev = self.head
            while current:
                prev = current
                if index == 1:
                    prev.next = current.next
                    current.next = None
                    return current.data
                current = current.next
                index -= 1
                print(index)
            return "Not found"

    def __len__(self):
        current = self.head
        length = 0
        while current:
            current = current.next
            length += 1
        return length

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next
        return '->'.join(map(str, nodes))


if __name__ == "__main__":
    ll = LinkedList()
    ll.preppend(1)
    ll.preppend(2)
    ll.preppend(3)
    ll.append(4)
    ll.append(5)
    print(ll)
    print(ll.pop(3))

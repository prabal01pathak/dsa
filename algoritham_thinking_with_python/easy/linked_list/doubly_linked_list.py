#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any

class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head: Node=None) -> None:
        self.head = head
        self.length = 0
        self.tail = head

    def append(self, node: Node) -> bool:
        if not self.head:
            self.head = node
            return True
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1
        return True

    def insert(self, pos: int, node: Node) -> bool:
        self.length += 1
        if not self.head:
            self.head = node
            self.length += 1
            return True
        if not pos:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return True
        if pos + 1 > self.length:
            self.append(node)
            self.length -= 1
            return True
        current = self.head
        i = 0
        while current:
            if pos == i:
                node.next = current
                node.prev = current.prev
                current.prev.next = node
                current.prev = node
                return True
            current = current.next
            i += 1
        return False

    def pop(self, pos: int=None) -> Any:
        if not pos:
            pos = self.length
            temp = self.tail
            prev = self.tail.prev
            prev.next = None
            temp.prev = None
            self.tail = prev
            self.length -= 1
            return temp
        if (self.length - pos) < self.length/2:
            print("here")
            current = self.tail
            i = self.length -1
            while current:
                if pos == i:
                    temp = current
                    prev = current.prev
                    prev.next = current.next
                    current.next.prev = prev
                    temp.next = None
                    temp.prev = None
                    self.length -= 1
                    print(temp.val)
                    return temp
                current = current.prev
                i -= 1
        current = self.head
        i = 0
        while current:
            if pos == i:
                temp = current
                prev = current.prev
                prev.next = current.next
                current.next.prev = prev
                temp.next = None
                temp.prev = None
                self.length -= 1
                return temp
            current = current.next
            i += 1
        return None


    def popleft(self):
        if not self.head:
            raise "Empty Linked List"
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        return temp

    def create_list(self, arr: list) -> None:
        if not len(arr):
            raise "Array empty"
        self.head = Node(arr[0])
        self.tail = self.head
        current = self.head
        for i in range(1, len(arr)):
            node = Node(arr[i])
            current.next = node
            node.prev = current
            current = current.next
        self.tail = current
        self.length = len(arr)

    def __repr__(self):
        if not self.head:
            return None
        current = self.head
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return f"DoublyLinkedList({res})"

    def __len__(self):
        return self.length


def test_doubly_linked_list():
    head = Node(4)
    dll = DoublyLinkedList(head)
    dll.append(Node(7))
    dll.insert(1, Node(9))
    dll.insert(2, Node(9))
    dll.insert(0, Node(9))
    dll.insert(0, Node(9))
    dll.append(Node(8))
    dll.append(Node(8))
    print(dll)
    dll.append(Node(8))
    print(dll.pop(3).prev)
    print(dll)


if __name__ == "__main__":
    test_doubly_linked_list()
    print("=================== All test passed =======================")

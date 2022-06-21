#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, val: int=None) -> None:
        self.val = val
        self.ptr_diff = None

    def set_ptr_diff(self, p, n):
        """
            p: previous Node
            n: next Node
        """
        self.ptr_diff = p ^ n


class Mlinked_list:
    def __init__(self, head: Node=None):
        self.head = head


def test_mlinked_list():
    node = Node(3)
    p = Node(4)
    n = Node(5)
    node.set_ptr_diff(4,6)
    print(node.ptr_diff)


if __name__ == "__main__":
    test_mlinked_list()


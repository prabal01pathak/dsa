#!/usr/bin/env python
# -*- coding: utf-8 -*-

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root):
    def validate(root, left, right):
        if not root:
            return True
        if not (left< root.data < right):
            return False
        return validate(root.left, left, root.data) and validate(root.right, root.data, right)
    return validate(root, float("-inf"), float("inf"))



def test_checkBST():
    root = node(10)
    root.left = node(5)
    root.right = node(15)
    root.left.left = node(1)
    root.left.right = node(6)
    root.right.left = node(11)
    root.right.right = node(20)
    assert checkBST(root) == True


if __name__ == "__main__":
    test_checkBST()
    print("==================== Tests passed ==========================")

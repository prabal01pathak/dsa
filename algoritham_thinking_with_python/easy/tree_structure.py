#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, x):
        if self.root is None:
            self.root = TreeNode(x)
        else:
            self.add_node(self.root, x)

    def add_node(self, node, x):
        if x < node.val:
            if node.left is None:
                node.left = TreeNode(x)
            else:
                self.add_node(node.left, x)
        else:
            if node.right is None:
                node.right = TreeNode(x)
            else:
                self.add_node(node.right, x)

    def print_tree(self):
        print("Tree:")
        self.print_node(self.root)

    def print_node(self, node):
        if node is not None:
            # print as tree
            print("\t" * (node.val + 1), node.val)
            self.print_node(node.left)
            self.print_node(node.right)

    def create_tree(self, arr):
        for x in arr:
            self.add(x)


def test_tree():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(1)
    tree.add(4)
    tree.add(2)
    tree.add(6)
    tree.add(7)
    tree.print_tree()

if __name__ == "__main__":
    test_tree()

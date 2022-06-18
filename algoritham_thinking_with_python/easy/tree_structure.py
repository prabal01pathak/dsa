#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

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

    def print_tree(self, node, result):
        if not node:
            return None
        queue = deque([ node ])
        while queue:
            root = queue.popleft()
            result.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return result

    def create_tree(self, arr):
        # arr: [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right ...]
        if not arr:
            return None
        root = TreeNode(arr[0])
        queue = deque([ root ])
        for i, node_val in enumerate(arr):
            if not i:
                continue
            if node_val:
                node = TreeNode(node_val)
            else:
                node = None
            if i%2:
                root_node = queue.popleft()
                root_node.left = node
            else:
                root_node.right = node
            if node:
                queue.append(node)
        return root

##             1
##            / \ 
##           /   \
##         3      2
##        /        \
#        /          \
#        4           5
#      /  \           \
#     /    \           \
#    6      7           9


def test_tree():
    tree = Tree()
    arr = [1,3,2,4, None, None, 5, 6, 7, None, 9]
    root = tree.create_tree(arr)
    tree.root = root
    print(tree.print_tree(root, []))

if __name__ == "__main__":
    test_tree()

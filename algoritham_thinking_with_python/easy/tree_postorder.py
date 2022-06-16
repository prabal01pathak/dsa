#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from tree_structure import TreeNode


class PostOrder:
    def postorder_iterative(self, root):
        if not root:
            return []
        visited = set()
        stack = []
        result = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.val)
                    node = None
        return result

    def postorder_recursive(self, root, result):
        if not root:
            return []
        self.postorder_recursive(root.left, result)
        self.postorder_recursive(root.right, result)
        result.append(root.val)
        return result


def test_postorder_traversal():
    postorder = PostOrder()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = []
    assert postorder.postorder_iterative(root) == [2, 3, 1]
    assert postorder.postorder_recursive(root, result) == [2, 3, 1]
    root = TreeNode(1)
    result = []
    assert postorder.postorder_iterative(root) == [1]
    assert postorder.postorder_recursive(root, result) == [1]

if __name__ == '__main__':
    test_postorder_traversal()

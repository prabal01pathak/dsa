#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from tree_structure import TreeNode

class LevelOrder:
    def level_order_iterative(sefl, root):
        if not root:
            return []
        queue = deque([ root ])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


def test_level_order_travers():
    level = LevelOrder()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert level.level_order_iterative(root) == [1, 2, 3]
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert level.level_order_iterative(root) == [1, 2, 3, 4, 5]
    root = TreeNode(1)
    assert level.level_order_iterative(root) == [1]
    assert level.level_order_iterative(None) == []


if __name__ == '__main__':
    test_level_order_travers()
    print("====================== Test passed level_order_travers ======================")

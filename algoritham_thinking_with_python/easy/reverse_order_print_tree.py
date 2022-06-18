#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional
from collections import deque

from tree_structure import TreeNode


class Solution:
    def reverse_level_order_traversal(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        queue = deque([ root ])
        result_queue = deque()
        while queue:
            node = queue.popleft()
            result_queue.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result_queue


def test_reverse_level_order_traversal():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.reverse_level_order_traversal(root) == deque([3, 2, 1])
    root = None
    assert solution.reverse_level_order_traversal(root) == []
    root = TreeNode(1)
    assert solution.reverse_level_order_traversal(root) == deque([1])

if __name__ == "__main__":
    test_reverse_level_order_traversal()
    print(" ================ All test passed ================")


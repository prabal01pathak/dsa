#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import Optional
from tree_structure import TreeNode, Tree


class Solution:
    def find_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([ root ])
        depth = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


def test_find_depth():
    solution = Solution()
    tree = Tree()
    arr = [1,3,4,5, 4, 7, 9, 10]
    root = tree.create_tree(arr)
    assert solution.find_depth(root) == 4


if __name__ == "__main__":
    test_find_depth()
    print(" =============== All test passed ================== ")


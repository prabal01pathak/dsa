#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import Optional
from tree_structure import Tree, TreeNode

class Solution:
    def deepest_node(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([ root ])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return node.val


def test_deepest_node():
    s = Solution()
    arr = [1,3,5,6,7, 9, 3, 10]
    tree = Tree()
    root = tree.create_tree(arr)
    assert s.deepest_node(root) == 10
    arr.pop()
    assert s.deepest_node(root) == 3


if __name__ == "__main__":
    test_deepest_node()
    print("================ All test passed =================== ")

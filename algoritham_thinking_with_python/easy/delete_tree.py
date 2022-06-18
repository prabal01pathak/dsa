#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional
from tree_structure import TreeNode

class Solution:
    def delete_binary_tree(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        self.delete_binary_tree(root.left)
        self.delete_binary_tree(root.right)
        del root


def test_delete_binary_tree():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(solution.delete_binary_tree(root))
    print(root.val)


if __name__ == "__main__":
    test_delete_binary_tree()
    print(root.val)

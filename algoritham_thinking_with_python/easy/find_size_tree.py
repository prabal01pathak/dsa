#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import Optional
from tree_structure import TreeNode

class Solution:
    def find_size(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+ self.find_size(root.left) + self.find_size(root.right)


    def find_size_iter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [ root ]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count

    def bfs_find_size(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([ root ])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count

def test_find_size():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(9)
    print(s.bfs_find_size(root))


if __name__ == "__main__":
    test_find_size()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric_iter(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        left_tree = self.isMirror_iter(root.left)
        right_tree = self.isMirror_iter(root.right, identify="r")
        return  left_tree == right_tree

    def isMirror_iter(self, root, identify="l"):
        stack = [ root ]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if identify == "l":
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    stack.append(node.right)
                    stack.append(node.left)
            else:
                result.append(node)
        return result


def test_is_symmetric():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    assert s.isSymmetric_iter(root) == True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert s.isSymmetric_iter(root) == False


if __name__ == '__main__':
    test_is_symmetric()
    print("============== All Test Passed ================")

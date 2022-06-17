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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, sums: int = 0) -> bool:
        if not root:
            return 0
        sums += root.val
        left_sum = root.val + self.hasPathSum(root.left, targetSum)
        # if left_sum == targetSum:
        #     return True
        # right_sum = root.val + self.hasPathSum(root.right, targetSum)
        # if right_sum == targetSum:
        #     return True
        return left_sum  # True if left_sum == targetSum else False


def test_hashPathSum():
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(s.hasPathSum(root, 22))
    assert s.hasPathSum(root, 22) is True


if __name__ == "__main__":
    test_hashPathSum()

from math import inf
from collections import deque
from typing import Optional

from tree_structure import TreeNode


class Solution:
    def min_value(self, root: TreeNode) -> int:
        """dfs"""
        if not root:
            return None
        smallest = inf
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if smallest > node.val:
                smallest = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return smallest

    def min_value_recursive(self, root: TreeNode, smallest=inf) -> int:
        if not root:
            return inf
        left_min = self.min_value_recursive(root.left, smallest)
        right_min = self.min_value_recursive(root.right, smallest)
        return min(root.val, left_min, right_min)


def test_min_value():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    assert s.min_value(root) == 0
    print(s.min_value_recursive(root))
    root = TreeNode(1)
    assert s.min_value(root) == 1
    root = None
    assert s.min_value(root) is None


if __name__ == "__main__":
    test_min_value()

"""
Description: find the sum of values in the given tree.
Author: Prabal Pathak
"""
import time
from collections import deque
from tree_structure import TreeNode


class Solution:
    def sum_tree(self, root: TreeNode) -> int:
        """sum the tree

        Args:
            root (TreeNode): root of the tree

        Returns:
            int: sum of the values in the tree
        """
        if not root:
            return 0
        return root.val + self.sum_tree(root.left) + self.sum_tree(root.right)

    def sum_tree_iterative(self, root: TreeNode) -> int:
        """Deapth first search"""
        if not root:
            return 0
        stack = [root]
        s = 0
        while stack:
            node = stack.pop()
            s += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return s

    def breadth_sum_tree(self, root: TreeNode) -> int:
        """Breadth first search"""
        if not root:
            return 0
        queue = deque([root])
        s = 0
        while queue:
            node = queue.popleft()
            s += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return s


def test_sum_tree():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)

    print(s.sum_tree(root))
    print(s.sum_tree_iterative(root))
    print(s.breadth_sum_tree(root))


if __name__ == "__main__":
    test_sum_tree()

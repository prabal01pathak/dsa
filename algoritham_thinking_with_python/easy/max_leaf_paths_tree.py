from collections import deque
from tree_structure import TreeNode


class Solution:
    def max_paths(self, root: TreeNode, target_value=0):
        if not root:
            return 0
        if not root.left and root.right:
            return root.val
        left_values = root.val + self.max_paths(root.left)
        right_values = root.val + self.max_paths(root.right)
        if target_value in (right_values, left_values):
            return True
        return left_values or right_values


def test_max_paths():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.left = TreeNode(10)
    print(s.max_paths(root, 1))


if __name__ == "__main__":
    test_max_paths()

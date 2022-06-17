from cgi import test
from tree_structure import TreeNode


class Solution:
    def traverse_tree(self, root, result):
        if not root:
            return None
        self.traverse_tree(root.left, result)
        result.append(root.val)
        self.traverse_tree(root.right, result)
        return result


def test_traverse_tree():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.left = TreeNode(5)
    print(s.traverse_tree(root, []))


if __name__ == "__main__":
    test_traverse_tree()

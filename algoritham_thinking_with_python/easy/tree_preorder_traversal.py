#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import List

from tree_structure import Tree, TreeNode

class PreOrderTraversal:
    def preorder_traversal(self, root, result: List[int] = None) -> List[int]:
        if root is None:
            return []
        result.append(root.val)
        self.preorder_traversal(root.left, result)
        self.preorder_traversal(root.right, result)
        print(result)
        return result

    def preorder_traversal_iterative(self, root):
        if not root:
            return []
        stack = [ root ]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


def test_preorder_traversal():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    preorder_traversal = PreOrderTraversal()
    assert preorder_traversal.preorder_traversal_iterative(root) == [1, 2, 4, 5, 3]


if __name__ == '__main__':
    test_preorder_traversal()

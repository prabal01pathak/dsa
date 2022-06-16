#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_structure import TreeNode

class Inorder:
    def inorder_traverse(self, root):
        if not root:
            return []
        stack = []
        result = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result

    def inorder_recursive(self, root, result):
        if not root:
            return []
        self.inorder_recursive(root.left, result)
        result.append(root.val)
        self.inorder_recursive(root.right, result)
        return result


def test_inorder():
    inorder = Inorder()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert inorder.inorder_traverse(root) == [4, 2, 5, 1, 6, 3, 7]
    assert inorder.inorder_recursive(root, []) == [4, 2, 5, 1, 6, 3, 7]
    root = TreeNode(1)
    assert inorder.inorder_traverse(root) == [1]
    assert inorder.inorder_recursive(root, []) == [1]
    assert inorder.inorder_traverse(None) == []
    assert inorder.inorder_recursive(None, []) == []

if __name__ == "__main__":
    test_inorder()

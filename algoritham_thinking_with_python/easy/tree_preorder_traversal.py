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


def test_preorder_traversal():
    tree = Tree()
    root = tree.create_tree([1, 2, 3, 4, 5, 6, 7])
    print(tree.print_tree())
    preorder_traversal = PreOrderTraversal()
    assert preorder_traversal.preorder_traversal(root) == [1, 2, 4, 5, 3, 6, 7]


if __name__ == '__main__':
    test_preorder_traversal()

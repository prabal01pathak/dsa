#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, x):
        if self.root is None:
            self.root = TreeNode(x)
        else:
            self.add_node(self.root, x)

    def add_node(self, node, x):
        if x < node.val:
            if node.left is None:
                node.left = TreeNode(x)
            else:
                self.add_node(node.left, x)
        else:
            if node.right is None:
                node.right = TreeNode(x)
            else:
                self.add_node(node.right, x)

    def print_tree(self):
        print("Tree:")
        self.print_node(self.root)

    def print_node(self, node):
        if node is not None:
            print("node:", node.val, end=", ")
            self.print_node(node.left)
            self.print_node(node.right)

    def create_tree(self, arr):
        if not arr:
            return
        st = []
        i = 1
        self.root = TreeNode(arr[0])
        st.append(self.root)
        while i < len(arr):
            if i%2 > 0:
                print("i:", i)
                if arr[i]:
                    node = st.pop(0)
                    left_node = TreeNode(arr[i])
                    node.left = left_node
                    st.append(node)
            else:
                if arr[i] and not arr[i-1]:
                    print("i None:", i)
                    node = st.pop(0)
                    right_node = TreeNode(arr[i])
                    node.right = right_node
                    st.append(node)
                elif arr[i]:
                    print("i not None:", i)
                    right_node = TreeNode(arr[i])
                    node.right = right_node
                    st.append(node)
            i += 1


def test_tree():
    tree = Tree()
    arr = [1,3,None,4]
    tree.create_tree(arr)
    tree.print_tree()

if __name__ == "__main__":
    test_tree()

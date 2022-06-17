#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from typing import Optional
from colorama import Fore

from tree_structure import TreeNode

class Solution:
    def find_value(self, root: TreeNode, value: int) -> Optional[TreeNode]:
        if not root:
            return False
        stack = [ root ]
        while stack:
            node = stack.pop()
            if node:
                if node.val == value:
                    return True
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return False



def test_find_value():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    show_progress_bar(0)
    assert s.find_value(root, 7) == True
    show_progress_bar(50)
    assert s.find_value(root, 8) == False
    show_progress_bar(100)

def show_progress_bar(per):
    print(Fore.GREEN + '\r[{0}] {1}%'.format('|' * (per // 2), per), end='')
    if per == 100:
        print('')

if __name__ == '__main__':
    test_find_value()
    print(f"{Fore.GREEN}Tests passed: {Fore.RED}{test_find_value.__name__}")

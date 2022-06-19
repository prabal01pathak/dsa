#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

def height(root):
    """
    Level order traversal: BFS
    """
    if not root:
        return 0
    queue = deque([ root ])
    height = -1
    while queue:
        height += 1
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return height


def test_height():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    assert height(root) == 3


if __name__ == '__main__':
    test_height()
    print(" ================= ALL TESTS PASSED ================= ")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           


def lca(root, v1, v2):
    #Enter your code here
    if not root:
        return None
    cur = root
    while cur:
        if cur.info > v1 and cur.info > v2:
            cur = cur.left
        elif cur.info < v1 and cur.info < v2:
            cur = cur.right
        else:
            return cur
    
    

def test_lca():
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
    assert lca(root, 8, 11).info == 8


if __name__ == '__main__':
    test_lca()

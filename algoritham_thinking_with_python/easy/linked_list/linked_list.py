#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: Linked List class
Author: Prabal Pathak
"""

from typing import Any, Optional

class Node:
    """
    Node class
    """
    def __init__(self, val: Any) -> None:
        """
        Initelize the node with val and next pointer
        """
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head: Optional[Node]=None) -> None:
        """
        Initilize the linked list class with or without head
        """
        self.head = head
        self.length = 0

    def insert_at_beg(self, node: Node)-> str:
        """
        Insert at the begginning of linked list 
        """
        if not self.head:
            self.head = node
            return "No Head Found: set head to node"
        node.next = self.head
        self.head = node
        self.length += 1
        return "Inserted"

    def insert_at_end(self, node: Node) -> str:
        """
        Insert at the end
        Args:
            node(Node): node to insert
        Return:
            str: Acknowledgement
        """
        if not self.head:
            self.head = node
            return "No Node found: set head to node"
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        self.length += 1
        return "Inserted at end"
    
    def insert_at_pos(self, pos: int, node: Node)-> bool:
        """
        Insert at the given position
        Args:
            pos(int): Position to insert min 1
            node(Node): Node to insert
        Return:
            bool: if inserted return true otherwise raise exception
        """
        if not self.head:
            raise "Inserting without head"
        if not pos -1:
            self.insert_at_beg(node)
            return True
        if pos > self.length:
            self.insert_at_end(node)
            return True
        current = self.head
        prev = self.head
        i = 0
        while pos - 1> i:
            prev = current
            current = current.next
            i += 1
        node.next = current
        prev.next = node
        self.length += 1
        return True

    def insert_after_value(self, value: Any, node: Node) -> bool:
        """
        insert after the given value
        Args:
            value(Any): value before insert node
            node(Node): node to insert
        Return:
            bool : Acknowledgement
        """
        if not self.head:
            raise False
        current = self.head
        while current:
            if current.val == value:
                node.next = current.next
                current.next = node
                self.length += 1
                return True
            current = current.next
        return False

    def delete_from_beg(self):
        """
        delete from the begginning
        """
        if not self.head:
            return "Don't have head"
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def delete_from_end(self):
        """
        Delete from the end from linked list
        """
        if not self.head:
            return None
        if not self.head.next:
            temp = self.head
            self.head = None
            self.length -= 1
            return temp
        current = self.head
        prev = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        self.length -= 1
        return current

    def delete_after_pos(self, pos: int) -> Node:
        """
        Delete the node in the gived position
        Args:
            pos(int): Position to delete
        Return:
            bool : deleted or not
        """
        if not self.head:
            raise "Empty head"
        if not pos -1:
            return self.delete_from_beg()
        if pos == self.length:
            print(self.length)
            return self.delete_from_end()
        current = self.head
        prev = self.head
        i = 0
        while current.next:
            prev = current
            current = current.next
            i += 1
            if pos - 1 == i:
                prev.next = current.next
                current.next = None
                return current
        return False

    def create_from_list(self, arr: list) -> Node:
        """
        Create linked list from list
        Args:
            arr(list): List of the values
        Return:
            bool: Acknowledgement
        """
        if not len(arr):
            return False
        self.head = Node(arr[0])
        current = self.head
        self.length = len(arr)
        for i in range(1, len(arr)):
            current.next = Node(arr[i])
            current = current.next
        return True

    def print_list(self) -> str:
        """
        Print the linked list structure
        """
        if not self.head:
            return
        res = []
        current = self.head
        while current:
            res.append(current.val)
            current = current.next
        return " --> ".join(map(str,res))


def test_linked_list() -> None:
    """
    Testing all the functions of linked list class
    """
    ll = LinkedList()
    head = Node(1)
    ll.length = 1
    ll.head = head
    ll.insert_at_end(Node(2))
    ll.insert_at_beg(Node(2))
    ll.insert_at_end(Node(3))
    ll.insert_after_value(1, Node(7))
    assert ll.insert_at_pos(4, Node(5)) == True
    assert ll.delete_from_beg().val == 2
    assert ll.delete_from_end().val == 3
    assert ll.delete_after_pos(8) == False
    assert ll.create_from_list([1,2,3,4]) == True
    print(ll.print_list())


if __name__ == "__main__":
    test_linked_list()
    print(" ====================== All test passed =========================")

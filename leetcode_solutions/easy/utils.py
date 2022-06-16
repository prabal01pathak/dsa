#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(linked_list):
    """
    Convert linked list to list.
    """
    if linked_list is None:
        return []
    else:
        return [linked_list.val] + to_list(linked_list.next)

def to_linked_list(lst):
    """
    Convert list to linked list.
    """
    if lst is None or len(lst) == 0:
        return None
    else:
        return ListNode(lst[0], to_linked_list(lst[1:]))

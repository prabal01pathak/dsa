#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linked_list import LinkedList, Node

def check_palindrome(head):
    if not head:
        return True
    slow_ptr = head
    fast_ptr = head
    stack = []
    flag = None
    i = 0
    while slow_ptr:
        if not fast_ptr.next or not fast_ptr.next.next:
            if not fast_ptr.next:
                if not i:
                    i += 1
                    slow_ptr = slow_ptr.next
                    continue
                prev = stack.pop()
                if slow_ptr.val != prev:
                    return False
            else:
                if not i:
                    stack.append(slow_ptr.val)
                else:
                    prev = stack.pop()
                    if slow_ptr.val != prev:
                        return False
            slow_ptr = slow_ptr.next
            i += 1
        else:
            stack.append(slow_ptr.val)
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
    return True


def test_check_palindrome():
    ll = LinkedList()
    l = [4,5,6,7,6,5,4]
    ll.create_from_list(l)
    assert check_palindrome(ll.head) == True
    l.pop()
    ll.create_from_list(l)
    assert check_palindrome(ll.head) == False
    assert check_palindrome(None) == True
    assert check_palindrome(Node(4)) == True
    l2 = [2,3]
    ll.create_from_list(l2)
    assert check_palindrome(ll.head) == False

if __name__ == "__main__":
    test_check_palindrome()

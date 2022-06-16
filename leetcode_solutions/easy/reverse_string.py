#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s)//2):
            s[index], s[-(index+1)] = s[-(index+1)], s[index]


def test_reverse_string():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
    print("--------------------- Test reverseString ---------------------")


if __name__ == '__main__':
    test_reverse_string()

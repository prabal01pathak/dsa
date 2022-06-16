#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)


def test_can_construct():
    s = Solution()
    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True
    print("========================================= Test Passed =========================================")


if __name__ == "__main__":
    test_can_construct()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, x in enumerate(s):
            if s.count(x) == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        for v in d:
            if d[v] == 1:
                return s.index(v)
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))

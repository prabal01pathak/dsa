#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def minDeletions(self, s: str) -> int:
        f = [0]*26
        for char in s:
            f[ord(char) - ord('a')] += 1
        delete_count = 0
        seen_hash = set()
        for i in f:
            if i in seen_hash:
                while i in seen_hash:
                    i -= 1
                    delete_count += 1
            if i:
                seen_hash.add(i)
        return delete_count



def test_minDeletions():
    s1 = "aaabbb"
    s2 = "abababcbcbdvssgvsssdfjsdfdk"
    solution = Solution()
    assert solution.minDeletions(s1) == 1
    solution.minDeletions(s2) == 6


if __name__ == "__main__":
    test_minDeletions()
    print("==================== All test passed ==========================")

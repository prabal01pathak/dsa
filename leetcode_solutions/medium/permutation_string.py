#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        if s1_counter == s2_counter:
            return True
        for i in range(len(s2) - len(s1)):
            s2_counter[s2[i]] -= 1
            if s2_counter[s2[i]] == 0:
                del s2_counter[s2[i]]
            s2_counter[s2[i + len(s1)]] += 1
            if s1_counter == s2_counter:
                return True
        return False


def test_checkInclusion():
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
    assert s.checkInclusion("adc", "dcda") == True
    assert s.checkInclusion("abcd", "abcdabcdabcdabcdabcdabcdabcdabc") == True
    assert s.checkInclusion("hello", "ooolleoooleh") == False
    print("========================== Test Passed ==========================")


if __name__ == '__main__':
    test_checkInclusion()

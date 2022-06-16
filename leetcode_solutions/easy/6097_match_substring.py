#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional, List

# 6097. Match Substring
# https://leetcode.com/problems/match-substring/
class Solution:
    def match_substring(self, s: str, sub: str, mappings: List[List[str]]) -> Optional[int]:
        new_str = ""
        visited_char = set()
        for c in sub:
            if c in visited_char:
                new_str += c
                continue
            elif True:
                visited_char.add(c)
            for mapping in mappings:
                if c == mapping[0]:
                    new_str += mapping[1]
                    break
            else:
                new_str += c
        print(new_str)
        print(new_str in s)
        print(visited_char)
        return True if new_str in s else False


def test_match_substring():
    s = "abbab"
    sub = "ab"
    mappings = [["a", "b"], ["b", "a"]]
    assert Solution().match_substring(s, sub, mappings) == True
    s = "fool3e7bar"
    sub = "leet"
    mappings = [["e","3"],["t","7"],["t","8"]]
    assert Solution().match_substring(s, sub, mappings) == True


if __name__ == '__main__':
    test_match_substring()

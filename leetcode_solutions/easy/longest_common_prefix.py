#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 1:
            return strs[0]
        common = strs[0]
        string = ''
        i = 0
        while i < length:
            if not i == length -1 :
                min_length = min(len(common), len(strs[i+1]))
                for j in range(min_length):
                    if common[j] == strs[i+1][j]:
                        string += common[j]
                    else:
                        break
                common = string
                string = ''
            i += 1
        print(common)
        return common

def test_longest_common_prefix():
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"

if __name__ == '__main__':
    test_longest_common_prefix()

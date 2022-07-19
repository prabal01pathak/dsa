#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_tri = []
        for i in range(numRows):
            prev = []
            if not i:
                pascal_tri.append([1])
                continue
            elif i == 1:
                pascal_tri.append([1, 1])
                continue
            else:
                pascal_prev = pascal_tri[-1]
                for j, value in enumerate(pascal_prev):
                    if not j:
                        prev.append(value)
                    else:
                        prev.append(value + pascal_prev[j - 1])
                        if j == len(pascal_prev) - 1:
                            prev.append(1)
            pascal_tri.append(prev)
        return pascal_tri


def test_generate():
    s = Solution()
    assert s.generate(1) == [[1]]
    assert s.generate(2) == [[1], [1,1]]
    assert s.generate(3) == [[1], [1,1], [1,2,1]]
    assert s.generate(4) == [[1], [1,1], [1,2,1], [1,3,3,1]]


if __name__ == "__main__":
    test_generate()
    print("="*10, " All test Passed ", "="*10)

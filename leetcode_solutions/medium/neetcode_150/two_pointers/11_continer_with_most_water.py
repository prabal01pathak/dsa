#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[r], height[l])
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


def test_maxarea():
    s = Solution()
    height = [1, 8, 9, 7, 8, 9]
    assert s.maxArea(height) == 32


if __name__ == "__main__":
    test_maxarea()
    print("\n\n", "="*10, " All test passed ", "="*10, "\n\n")

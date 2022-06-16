#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ins = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ins.append(nums1[i])
                    nums2.pop(j)
                    break
        return ins


def test_intersection_two_array():
    s = Solution()
    assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert s.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]


if __name__ == '__main__':
    test_intersection_two_array()

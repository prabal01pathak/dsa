#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_array = []
        l = 0
        b = len(nums) - 1
        length = len(nums)
        for index in range(len(nums)):
            if index == length - 1:
                sorted_array.insert(0,pow(nums[l],2))
            elif abs(nums[l]) > abs(nums[b]) :
                sorted_array.insert(0,pow(nums[l],2))
                l += 1
            else:
                sorted_array.insert(0,pow(nums[b],2))
                b -= 1
        return sorted_array

def test_sorted_squares():
    s = Solution()
    assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]


if __name__ == '__main__':
    test_sorted_squares()

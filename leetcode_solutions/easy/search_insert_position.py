#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        first_index = 0
        last_index = len(nums) - 1
        while first_index <= last_index:
            midpoint = (first_index + last_index)//2
            if nums[midpoint] == target: 
                return midpoint
            elif nums[midpoint] > target:
                last_index = midpoint - 1
            else:
                first_index = midpoint + 1
        if nums[midpoint] > target:
            if nums[midpoint - 1] < target:
                return midpoint
            return midpoint -1
        return midpoint + 1


def test_search_insert_position():
    s = Solution()
    print(s.searchInsert([1,3], 2))
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6],0) == 0
    assert s.searchInsert([1,3], 2) == 1
    print('----------------------\nALL TEST PASSED')

if __name__ == '__main__':
    test_search_insert_position()

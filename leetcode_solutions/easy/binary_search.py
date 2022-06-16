#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1
        index = 0
        while index < len(nums):
            midpoint = (first_index + last_index) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                last_index = midpoint - 1
            else:
                first_index = midpoint + 1
            index += 1
        return -1


def test_binary_search():
    s = Solution()
    assert s.search([1, 2, 3, 4, 5], 3) == 2
    assert s.search([1, 2, 3, 4, 5], 6) == -1
    assert s.search([1, 2, 3, 4, 5], 0) == -1
    assert s.search([1, 2, 3, 4, 5], 5) == 4
    assert s.search([1, 2, 3, 4, 5], 1) == 0
    assert s.search([1, 2, 3, 4, 5], 2) == 1
    print('All tests passed.')


if __name__ == '__main__':
    test_binary_search()


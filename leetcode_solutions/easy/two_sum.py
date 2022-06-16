#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index in range(len(nums)):
            required_value = target - nums[index]
            if required_value in hash_table:
                value = [hash_table[required_value], index]        
                return value
            hash_table[nums[index]] = index
        return []



def test_two_sum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("------------------------------- All test passed -------------------------------------")


if __name__ == '__main__':
    test_two_sum()

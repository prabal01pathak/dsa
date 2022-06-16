#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        moved = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                moved += 1
            else:
                i += 1
            if i + moved >= len(nums):
                break
        return 


def test_move_zeros():
    s = Solution()
    nums = [0,1,0,3,12]
    s.moveZeroes(nums)
    assert nums == [1,3,12,0,0]
    nums = [0,0,1]
    s.moveZeroes(nums)
    assert nums == [1,0,0]
    nums = [0,0]
    s.moveZeroes(nums)
    assert nums == [0,0]
    nums = [1]
    s.moveZeroes(nums)
    assert nums == [1]
    nums = [0,0,0,0,0,0,0,2,3,5,4,0,0,0,23,0,0]
    s.moveZeroes(nums)
    assert nums == [2,3,5,4,23,0,0,0,0,0,0,0,0,0,0,0,0]
    nums = [0,0,0,0,0,2,3,0,0,0,0,0,234,0,0]
    s.moveZeroes(nums)
    assert nums == [2,3,234,0,0,0,0,0,0,0,0,0,0,0,0]
    print('------------------------------- test_move_zeros -------------------------------')


if __name__ == '__main__':
    test_move_zeros()
        

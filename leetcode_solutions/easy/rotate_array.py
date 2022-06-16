#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        index = len(nums) - k
        k_nums = nums[index:]
        del nums[index:]
        nums[:] = k_nums + nums
        return 
    
    
    
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            append_value = nums.pop()
            nums.insert(0,append_value)
        return


def test_solution():
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]
    nums = [1,2,3,4,5,6,7]
    k = 1
    Solution().rotate(nums, k)
    assert nums == [7,1,2,3,4,5,6]


if __name__ == '__main__':
    test_solution()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        first_point = 0
        second_point = 0
        third_point = 0
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum += nums[i]
            else:
                first_point = i
                second_point = i
                current_sum = nums[i]

            if current_sum > max_sum:
                max_sum = current_sum
                second_point = i
        return max_sum

def test_easy_maximum_subarray():
    s = Solution()
    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == [4,-1,2,1]
    assert s.maxSubArray([-2,1]) == [1]
    assert s.maxSubArray([-2,1,-3]) == [1]

if __name__ == '__main__':
    test_easy_maximum_subarray()

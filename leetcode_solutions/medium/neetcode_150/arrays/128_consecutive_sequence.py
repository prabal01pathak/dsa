#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in num_set:
                length = 0
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest

def test_longest_consecutive():
    s = Solution()
    nums = [100,4,200,1,3,2]
    assert s.longestConsecutive(nums) == 4
    nums = [0,3,7,2,5,8,4,6,0,1]
    assert s.longestConsecutive(nums) == 9


if __name__ == "__main__":
    test_longest_consecutive()
    print("="*10, " All test passed ", "="*10)

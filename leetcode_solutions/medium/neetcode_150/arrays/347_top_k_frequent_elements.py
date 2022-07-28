#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

# solved with bucket sort
# neetcode.io
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_hash = {}
        freq = [[] for _ in range(len(nums) + 1)]
        # collect count
        for num in nums:
            result_hash[num] = result_hash.get(num, 0) + 1
        
        # bucket sort with count
        for n, c in result_hash.items():
            freq[c].append(n)
        
        res = []
        # check res and append that
        for i in range(len(freq) -1 , 0, -1):
            if freq[i]:
                for item in freq[i]:
                    res.append(item)
                    if len(res) == k:
                        return res


def test_topkFrequent():
    s = Solution()
    arr = [1,1,1,2,2,3]
    k = 2
    assert s.topKFrequent(arr, k) == [1,2]
    arr = [1]
    k = 1
    assert s.topKFrequent(arr, k) == [1]


if __name__ == "__main__":
    test_topkFrequent()
    print("="*10, "All Test Passed", "="*10)

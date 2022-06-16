# usr/bin
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1 = nums2
            return nums1
        if n == 0:
            return nums1
        nums1 = nums1[:m]
        length_nums1 = len(nums1)
        length_nums2 = len(nums2)
        iter_nums1 = iter(nums1)
        iter_nums2 = iter(nums2)
        nums1_pointer = next(iter_nums1)
        nums2_pointer = next(iter_nums2)
        nums1_index = 0
        nums2_index = 0
        while True:
            if nums1_pointer > nums2_pointer:
                if nums1_index == length_nums1:
                    nums1 += nums2[nums2_index:]
                    return nums1
                # nums1.insert(nums1_pointer, nums1_index)
                nums1.insert(nums1_index, nums2_pointer)
                nums2_pointer = next(iter_nums2)
                nums2_index += 1
            else:
                if nums1_index == length_nums1 and nums2_index < length_nums2:
                    nums1 += nums2[nums2_index:]
                    return nums1
                nums1_pointer = next(iter_nums1)
                nums1_index += 1


def test_merge():
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums11 = [1, 2, 3, 5, 6]
    m1 = 3
    nums12 = []
    m2 = 0
    nums21 = []
    n1 = 0
    assert s.merge(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]
    assert s.merge(nums11, m1, nums2, n) == [1, 2, 2, 3, 5, 6]
    assert s.merge(nums1, m, nums21, n1) == nums1
    result = s.merge(nums12, m2, nums2, n)
    assert s.merge(nums12, m2, nums2, n) == nums2


if __name__ == '__main__':
    test_merge()

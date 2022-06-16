#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

# reshape matrix
class Solution:
    def matrixReshape(self, nums, r, c):
        if len(nums) * len(nums[0]) != r * c:
            return nums
        p = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        return [p[i:i+c] for i in range(0, len(p), c)]

class Solution2:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c or (len(mat) == r and len(mat[0]) == c):
            return mat
        mat_1d = [[]]
        for i in mat:
            mat_1d[0].extend(i)
        r_mat = []
        f = 0
        l = c
        for values in range(r):
            r_mat.append(mat_1d[0][f:l])
            f += c
            l += c
        return r_mat



def test_solution():
    solution = Solution()
    assert solution.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
    assert solution.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
    assert solution.matrixReshape([[1, 2], [3, 4]], 4, 1) == [[1], [2], [3], [4]]
    assert solution.matrixReshape([[1, 2], [3, 4]], 4, 2) == [[1, 2], [3, 4]]
    assert solution.matrixReshape([[1, 2], [3, 4]], 4, 3) == [[1, 2, 3], [4, 0, 0]]


if __name__ == '__main__':
    test_solution()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]
        res = []
        top = left = 0
        bottom = len(matrix)
        right = len(matrix[0])
        while left< right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right -1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            
            bottom -= 1
            
            for i in range(bottom -1 , top -1, -1):
                res.append(matrix[i][left])
            
            left += 1
        return res


def test_spiral_matrix():
    s = Solution()
    assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
    assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]


if __name__ == '__main__':
    test_spiral_matrix()
    print(" =================== All Tests Passed =================== ")

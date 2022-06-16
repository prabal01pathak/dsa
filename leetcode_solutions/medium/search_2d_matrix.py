#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[len(row) - 1]:
                low = 0
                high = len(row) - 1
                while high >= low:
                    midpoint = (high + low) // 2
                    if row[midpoint] == target:
                        return True
                    elif row[midpoint] > target:
                        high = midpoint - 1
                    else:
                        low = midpoint + 1
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    

def test_search_2d_matrix():
    s = Solution()
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3) == True
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13) == False
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0) == False
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 50) == True
    print('---------------------- Test Passed ----------------------')


if __name__ == '__main__':
    test_search_2d_matrix()

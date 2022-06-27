#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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


def test_searchMatrix():
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert s.searchMatrix(matrix, 3) == True
    assert s.searchMatrix(matrix, 5) == True
    assert s.searchMatrix(matrix, 15) == False


if __name__ == "__main__":
    test_searchMatrix()
    print("======================== All test passed ================================")

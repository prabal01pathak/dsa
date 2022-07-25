#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, grid = defaultdict(list), defaultdict(list), defaultdict(list)
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue
                x, y = i//3, j//3
                if c in row[i] or c in column[j] or c in grid[(x,y)]:
                    return False
                row[i].append(c)
                column[j].append(c)
                grid[(x,y)].append(c)
        return True

board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.isValidSudoku(board))

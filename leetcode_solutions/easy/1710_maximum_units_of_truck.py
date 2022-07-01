#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes,key=lambda x:x[1], reverse=True)
        total_units = 0
        for box in sorted_box:
            count = box[0]
            remain = truckSize - count
            if remain >0:
                total_units += count*box[1]
            else:
                total_units += truckSize*box[1]
                break
            truckSize = remain
        return total_units


def test_maximumUnits():
    s = Solution()
    boxes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    assert s.maximumUnits(boxes, truckSize) == 91


if __name__ == "__main__":
    test_maximumUnits()
    print("================= All test passed ======================")


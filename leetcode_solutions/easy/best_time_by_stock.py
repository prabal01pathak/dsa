#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy_day = prices[0]
        sell_day = 0
        profit = 0 
        for price in prices:
            if price - buy_day > profit:
                sell_day = price
                profit = price - buy_day
            elif price < buy_day :
                buy_day = price 
        return profit


def test_best_time_by_stock():
    s = Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0
    assert s.maxProfit([2]) == 0
    assert s.maxProfit([1]) == 0


if __name__ == '__main__':
    test_best_time_by_stock()

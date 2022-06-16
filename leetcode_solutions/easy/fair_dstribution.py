#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

 

Example 1:

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
"""

class Solution:
    def findMinUnfairness(self, cookies: List[int], k: int) -> int:
        if not cookies or not k:
            return 0
        if k == 1:
            return sum(cookies)
        cookies.sort()
        unfairness = float('inf')
        left = 0
        right = sum(cookies)
        for i in range(k):
            unfairness = min(unfairness, right - left)
            left += cookies[i]
            right -= cookies[i]
        return unfairness

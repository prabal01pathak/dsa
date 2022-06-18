#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def fabonacci_number(self, n, start = 1):
        if start == n:
            return n
        return 1 + fabonacci_number(n, start+1)

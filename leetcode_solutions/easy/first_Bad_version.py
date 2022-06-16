#!/usr/bin/env python
# -*- coding: utf-8 -*-

BAD_VERSIONS = [3,5,2,8,9,10,58,7]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        first_version = 0
        last_version = n
        while 0 < n:
            midpoint = (first_version + last_version) // 2
            if midpoint != 1 and isBadVersion(midpoint) and not isBadVersion(midpoint - 1):
                return midpoint
            elif isBadVersion(midpoint - 1):
                last_version = midpoint - 1
            else:
                first_version = midpoint + 1
            
            n -= 1
        return 0
                
            
            
def isBadVersion(n):
    if n in BAD_VERSIONS:
        return True
    return False

def test_first_bad_version():
    s = Solution()
    assert s.firstBadVersion(4) == 2
    assert s.firstBadVersion(5) == 2
    assert s.firstBadVersion(6) == 2
    assert s.firstBadVersion(7) == 2
    print('Tests passed.')


if __name__ == '__main__':
    test_first_bad_version()

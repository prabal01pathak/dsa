#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rotate_matrix(m):
    arr = []
    for i in range(len(m[0])):
        arr.append([])
    for i in range(len(m)):
        for j in range(0, len(m[0])):
            arr[-(j+1)].append(m[i][j])
    return arr


def test_rotate_matrix():
    n = [[1,2,3],[4,5,6], [7,8,9]]
    n2 = rotate_matrix(n)
    n3 = rotate_matrix(n2)
    n4 = rotate_matrix(n3)
    n5 = rotate_matrix(n4)
    print(n5)

if __name__ == "__main__":
    test_rotate_matrix()

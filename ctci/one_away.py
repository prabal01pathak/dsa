#!/usr/bin/env python
# -*- coding: utf-8 -*-

def one_away(w1: str, w2: str) -> bool:
    if len(w2) + 1 !=  len(w1) and len(w2) != len(w1):
        return False
    count = 0
    for i, j in zip(w1, w2):
        count += 1
        print(i, j)
        if i == j:
            continue
        if w1[count:] != w2[count:] and w1[count:] != w2[count-1:]:
            print(w2[count:])
            return False
        break
    return True


def test_one_away():
    print(one_away("palea", "pala"))


if __name__ == "__main__":
    test_one_away()

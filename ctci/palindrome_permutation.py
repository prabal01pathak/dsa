#!/usr/bin/env python
# -*- coding: utf-8 -*-

def permutation_palindrome(words: str) -> bool:
    words = words.lower()
    single = {}
    double = {}
    count = 0
    for i in range(len(words)):
        if words[i] == " ":
            continue
        if double.get(words[i], 0) > 0:
            double[words[i]] = double.get(words[i]) + 1
        elif single.get(words[i],0)>0:
            double[words[i]] = single.get(words[i]) + 1
            del single[words[i]]
        else:
            single[words[i]] = 1
        count += 1
    print(count)
    print(single)
    print(double)
    if not count%2:
        return not len(single)
    return len(single) == 1 or len(single) == 0


def test_permutation_palindrome():
    string = "Tact coa"
    print(permutation_palindrome(string))


if __name__ == "__main__":
    test_permutation_palindrome()

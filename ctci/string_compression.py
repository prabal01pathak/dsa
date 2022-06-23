#!/usr/bin/env python
# -*- coding: utf-8 -*-

def string_compression(w: str) -> str:
    new_str = ""
    ones = True
    for i in range(len(w)):
        if not i:
            current = w[i]
            count = 1
            continue
        if count > 1:
            ones = False
        if current == w[i]:
            count += 1
        else:
            new_str += f"{current}{count}"
            count = 1
            current = w[i]
        if i+1 == len(w):
            new_str += f"{current}{count}"
    return new_str if not ones else w


def test_string_compression():
    print(string_compression("aaaaasdskjfljfj"))
    print(string_compression("abcd"))

if __name__ == "__main__":
    test_string_compression()
